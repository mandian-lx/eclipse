%define _duplicate_files_terminate_build 0

# TODO:
# - update icu4j and jasper to use %%{_libdir}/eclipse and not %%{_datadir}/eclipse after we build 3.4
# - update ecj-rpmdebuginfo patch
# - look at startup script and launcher patches
# - get Ganymede update site pre-configured
# - investigate bi-arch requirements
# - see why about.html isn't being copied on ppc

%define eclipse_major   3
%define eclipse_minor   4
%define eclipse_majmin  %{eclipse_major}.%{eclipse_minor}
%define eclipse_micro   2
%define swtver          3.4.1.v3452b

# All arches line up between Eclipse and Linux kernel names except i386 -> x86
%ifarch %{ix86}
%define eclipse_arch    x86
%else
%define eclipse_arch   %{_arch}
%endif

%define initialize      1

Summary:        An open, extensible IDE
Name:           eclipse
Version:        %{eclipse_majmin}.%{eclipse_micro}
Release:        0.2.11
Epoch:		1
License:        EPL
Group:          Development/Java
URL:            http://www.eclipse.org/
Source0:        http://download.eclipse.org/eclipse/downloads/drops/R-3.4.2-200902111700/eclipse-sourceBuild-srcIncluded-%{version}.zip
Source1:	%{name}.rpmlintrc
Source2:        %{name}.desktop
#Source3:        eclipse.in
# cvs -d :pserver:anonymous@sources.redhat.com:/cvs/eclipse export \
#   -r fedoraeclipse-3_4_0-1 branding/org.fedoraproject.ide.platform
# cd branding
# zip -r org.fedoraproject.ide.platform-3.4.0-1.zip \
#   org.fedoraproject.ide.platform
Source4:        org.mandriva.ide.platform-%{version}.zip
# cvs -d :pserver:anonymous@sources.redhat.com:/cvs/eclipse export \
#   -r fedoraeclipsefeature-1_0_0 branding/org.fedoraproject.ide-feature
# cd branding
# zip -r org.fedoraproject.ide.feature-1.0.0.zip \
#   org.fedoraproject.ide-feature
Source5:        org.mandriva.ide.feature-1.0.0.zip
Source16:       %{name}-copy-platform.sh
Source17:       efj.sh.in
Source18:       ecj.sh.in
# This file contains the types of files we'd like to extract from the jars
# when using the FileInitializer
Source19:       %{name}-filenamepatterns.txt
# cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/eclipse co equinox-incubator/org.eclipse.equinox.initializer
# tar cjf eclipse-fileinitializerapp.tar.bz2 equinox-incubator/
# (generated 2006-11-01 18:48 UTC)
Source20:       %{name}-fileinitializerapp.tar.bz2
# Script to wrap PDE Build calls for bundle builds
Source21:       %{name}-pdebuild.sh
# config.ini to run the director for provisioning the installation
Source22:       %{name}-config.ini.director
Source24:       fetch-ecf.sh
# This was fetched using the above script.
# We will eventually have an eclipse-ecf package but since the ECF
# filetransfer bits that are part of the SDK actually require the SDK >=
# 3.4 to build, I'm going to build them here and have them be owned by
# the SDK packages for now. -- overholt, 2008-07-07
Source25:       ecf-filetransfer-v20080611-1715.tar.bz2
# Create a simple feature for building ECF's filetransfer plugins
Source26:       ecf-filetransfer-feature.xml
Source27:       ecf-filetransfer-build.properties
# This script copies the platform sub-set of the SDK for generating metadata
Source28:       %{name}-mv-Platform.sh
# Use ECJ for GCJ
# cvs -d:pserver:anonymous@sourceware.org:/cvs/rhug \
# export -r eclipse_r34_1 eclipse-gcj
# tar cjf eclipse-ecj-gcj.tar.bz2 eclipse-gcj
Source29:       %{name}-ecj-gcj.tar.bz2
# Test feature and plugins
# cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/eclipse co equinox-incubator/org.eclipse.equinox.initializer
# mkdir %{name}-%{version}-testframework; cd %{name}-%{version}-testframework
# cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/eclipse export -r R3_4 \
#   org.eclipse.test \
#   org.eclipse.test.performance \
#   org.eclipse.test-feature \
#   org.eclipse.ant.optional.junit
# tar cjf %{name}-%{version}-testframework.tar.bz2 \
#   %{name}-%{version}-testframework
# (generated 2008-08-27)
Source30:       %{name}-%{version}-testframework.tar.bz2

# Build swttools.jar before generation on 64-bit platforms.
# Build SWT native libraries
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=90364
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=221908
# https://bugs.eclipse.org/bugs/attachment.cgi?id=105593
Patch4:         %{name}-buildswtnatives.patch
Patch32:        %{name}-compilelibs.patch

# This does two things:
# 1. allows the launcher to be in /usr/bin and
# 2. ensures that the OSGi configuration directory
#    (which contains the JNI .sos) is in %{_libdir}
# We should investigate whether or not this can go upstream
#Patch12:        %{name}-launcher-set-install-dir-and-shared-config.patch
# Always generate debug info when building RPMs (Andrew Haley)
# This needs to be investigated for getEnv changes
# FIXME:  update this patch to avoid fuzz
Patch14:        %{name}-ecj-rpmdebuginfo.patch
# generic releng plugins that can be used to build plugins
# see this thread for details:
# https://www.redhat.com/archives/fedora-devel-java-list/2006-April/msg00048.html
Patch15:        %{name}-pde.build-add-package-build.patch
Patch24:        %{name}-add-ppc64-sparc64-s390-s390x.patch
Patch28:        %{name}-add-ppc64-sparc64-s390-s390x-2.patch
Patch30:        %{name}-addfragmentsforotherplatforms.patch
Patch38:        %{name}-addrootfiles.patch
#FIXME: file a bug upstream
Patch26:        %{name}-launcher-fix-java-home.patch
# Default max heap size too low for lots of people.  Bump to 512 MB.
# Max perm size:
# https://bugzilla.redhat.com/show_bug.cgi?id=352361
# JVM crash:
# http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=6614100
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=214092
Patch29:        %{name}-memorypermsizeandjvmcrash.patch

Patch31:	%{name}-ia64-packaging.patch

# FIXME:  file these upstream
# Upstream builds with a 1.4 (or lower) class library
# Patch33:	%{name}-pdeapicasting.patch
# Patch34:	%{name}-pdeapicasting-ui.patch

# Make ECF bundles have the same qualifier as they do upstream
Patch35:	%{name}-ecf-qualifier.patch

# Don't pack the icu4j source bundle.  Can go away when we re-build
# icu4j against a 3.4 SDK.
Patch36:	%{name}-dontpackicu4jsource.patch

# Our dependent JARs have different signatures than the ones included
# upstream so remove the signatures in the manifests
Patch37:	%{name}-nojarsignatures.patch

## Back-port patches from 3.4.x stream.  These will be in 3.4.1.
## https://bugs.eclipse.org/bugs/show_bug.cgi?id=242632
#Patch39:        %{name}-profilesync-e.o242632.patch
#Patch40:        %{name}-profilesync-e.o242632-2.patch

# Remove win32 fragment from test feature
Patch41:        %{name}-nowin32testfragment.patch

# Some fixes for library.xml
# FIXME:  submit upstream
Patch42:        %{name}-tests-libraryXml.patch

Patch43:		%{name}-osgi-classpath.patch
Patch44:		%{name}-fix-javahome64.patch

# Default to 1.5 source and bytecode
# https://bugzilla.redhat.com/354721
Patch45:		%{name}-ecj-defaultto1.5.patch
Patch46:	eclipse-3.4.0-CVE-2010-4647.diff

BuildRequires:  ant
BuildRequires:  jpackage-utils >= 0:1.5, make, gcc
BuildRequires:  gnome-vfs2-devel
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libgnome-2.0)
BuildRequires:  pkgconfig(libgnomeui-2.0)
BuildRequires:  gcc-c++
BuildRequires:  xulrunner-devel >= 1.9
BuildRequires:  nspr-devel
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  unzip
BuildRequires:  zip
BuildRequires:  icu4j-eclipse >= 3.8.1
BuildRequires:  tomcat5-jasper-eclipse >= 5.5.26-1.5
BuildRequires:  tomcat5-jsp-2.0-api
BuildRequires:  desktop-file-utils
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  java-rpmbuild
BuildRequires:  java-javadoc
BuildRequires:  libxt-devel

# Need to investigate why we don't build ant-apache-bsf or ant-commons-net in
# Fedora.  When that's done, add it here and symlink below.
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=180642
BuildRequires: ant-antlr ant-apache-bcel ant-apache-log4j ant-apache-oro ant-apache-regexp ant-apache-resolver ant-commons-logging
BuildRequires: ant-javamail ant-jdepend ant-junit ant-nodeps ant-swing ant-trax ant-jsch
BuildRequires: jsch >= 0:0.1.31
BuildRequires: jakarta-commons-beanutils jakarta-commons-collections jakarta-commons-digester jakarta-commons-dbcp jakarta-commons-fileupload jakarta-commons-launcher jakarta-commons-modeler jakarta-commons-pool
BuildRequires: jakarta-commons-el >= 1.0-8jpp
BuildRequires: jakarta-commons-logging >= 1.0.4-6jpp.3
BuildRequires: mx4j >= 2.1
BuildRequires: jetty5
BuildRequires: lucene >= 1.9.1
BuildRequires: lucene-contrib >= 1.9.1
BuildRequires: regexp
BuildRequires: junit >= 3.8.1-3jpp
BuildRequires: junit4
BuildRequires: sat4j
BuildRequires: asm3

%description
The Eclipse platform is designed for building integrated development
environments (IDEs), server-side applications, desktop applications, and
everything in between.

%package        ecj
Summary:        Eclipse Compiler for Java
Group:          Development/Java
Obsoletes:      ecj < 2:%{version}-%{release}
Obsoletes:      libecj-java < 2:%{version}-%{release}
Provides:       ecj = %{version}-%{release}
Provides:       libecj-java = %{version}-%{release}
Requires:       java >= 1.6.0

%description    ecj
Eclipse compiler for Java.

%package     swt
Summary:        SWT Library for GTK+-2.0
Group:          Development/Java
# %{_libdir}/java directory owned by jpackage-utils
Requires:       jpackage-utils
Requires:       gtk2
Requires:       xulrunner >= 1.9
#Conflicts:      mozilla
Provides:       libswt3-gtk2 = 1:%{version}-%{release}
# The 20 is more than the currently (2008-06-25) latest 3.3.2 package
# but I want to leave some room in case we need to do an F9 update.
Obsoletes:       libswt3-gtk2 < 1:3.3.2-20

%description swt
SWT Library for GTK+-2.0.

%package        rcp
Summary:        Eclipse Rich Client Platform
Group:          Development/Java
Requires:       %{name}-swt = %{epoch}:%{version}-%{release}
# FIXME:  investigate.  Can we just add a %{arch} to the above?
## This file-level requirement is for the bi-arch multilib case
#Requires: %{_libdir}/%{name}/plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}_%{swtver}.jar
Requires:       icu4j-eclipse >= 3.8.1
Requires:       java >= 1.6.0

%description    rcp
Eclipse Rich Client Platform

%package        platform
Summary:        Eclipse platform common files
Group:          Development/Java
Requires:   %{name}-rcp = %{epoch}:%{version}-%{release}
# FIXME:  investigate.  Can we just add a %{arch} to the above?
## This file-level requirement is for the bi-arch multilib case
#Requires: %{_libdir}/%{name}/plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}_%{swtver}.jar
# Need to investigate why we don't build ant-apache-bsf or ant-commons-net in
# Fedora.  When that's done, add it here and symlink below.
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=180642
#Requires: ant-apache-bsf ant-commons-net
Requires: ant-antlr ant-apache-bcel ant-apache-log4j ant-apache-oro ant-apache-regexp ant-apache-resolver ant-commons-logging
Requires: ant-javamail ant-jdepend ant-junit ant-nodeps ant-swing ant-trax ant-jsch
Requires: jakarta-commons-beanutils jakarta-commons-collections jakarta-commons-digester jakarta-commons-dbcp jakarta-commons-fileupload jakarta-commons-launcher jakarta-commons-modeler jakarta-commons-pool
Requires: jakarta-commons-el >= 1.0-8jpp
Requires: jakarta-commons-logging >= 1.0.4-6jpp.3
Requires: mx4j >= 2.1
Requires: tomcat5-jasper-eclipse >= 5.5.26-1.5
Requires: tomcat5-jsp-2.0-api
Requires: jetty5
Requires: jsch >= 0.1.31
Requires: lucene >= 1.9.1
Requires: lucene-contrib >= 1.9.1
Requires: regexp
Requires: sat4j
Provides: eclipse-cvs-client = 1:%{version}-%{release}
Obsoletes: eclipse-cvs-client < 1:3.3.2-20

%description    platform
The Mandriva Eclipse Platform is the base of all IDE plugins.
This does not include the Java Development Tools or the Plugin
Development Environment.

%package        jdt
Summary:        Eclipse Java Development Tools
Group:          Development/Java
Requires:       %{name}-platform = %{epoch}:%{version}-%{release}
Requires:       %{name}-cvs-client = %{epoch}:%{version}-%{release}
Requires:       %{name}-ecj = %{epoch}:%{version}-%{release}
Requires:       junit >= 3.8.1-3jpp
Requires:       junit4
Requires:       java-javadoc

%description    jdt
Eclipse Java Development Tools.  This package is required to use Eclipse for
developing software written in the Java programming language.

%package        pde
Summary:        Eclipse Plugin Development Environment
Group:          Development/Java
Provides:	eclipse-sdk
Provides:	eclipse
Requires:       %{name}-platform = %{epoch}:%{version}-%{release}
Requires:       %{name}-jdt = %{epoch}:%{version}-%{release}
Requires:       asm3
# For PDE Build wrapper script
Requires:       bash
Provides:       %{name}-pde-runtime = 1:%{version}-%{release}
# The 20 is more than the currently (2008-06-25) latest 3.3.2 package
# but I want to leave some room in case we need to do an F9 update.
Obsoletes:       %{name}-pde-runtime < 1:3.3.2-20

%description    pde
Eclipse Plugin Development Environment.  This package is required for
developing Eclipse plugins.

%prep
%setup -q -c

sed --in-place "s/java5.home/java.home/" build.xml
# Build swttools.jar and native libraries
%patch4 -p0
%patch32 -p0

# Fix swt library build with new xulrunner
sed --in-place "s/MOZILLACFLAGS =/MOZILLACFLAGS = -std=gnu++0x/" "plugins/org.eclipse.swt/Eclipse SWT PI/gtk/library/make_linux.mak"

# Use ECJ for GCJ's bytecode compiler
tar jxf %{SOURCE29}
mv eclipse-gcj/org/eclipse/jdt/internal/compiler/batch/GCCMain.java \
  plugins/org.eclipse.jdt.core/batch/org/eclipse/jdt/internal/compiler/batch/
cat eclipse-gcj/gcc.properties >> \
  plugins/org.eclipse.jdt.core/batch/org/eclipse/jdt/internal/compiler/batch/messages.properties
rm -rf eclipse-gcj

# liblocalfile fixes
sed --in-place "s/JAVA_HOME =/#JAVA_HOME =/" plugins/org.eclipse.core.filesystem/natives/unix/linux/Makefile
sed --in-place "s/OPT_FLAGS=-O/OPT_FLAGS=-O2 -g/" plugins/org.eclipse.core.filesystem/natives/unix/linux/Makefile

# launcher patches
rm plugins/org.eclipse.platform/launchersrc.zip
pushd features/org.eclipse.equinox.executable
#%patch12 -p0
%patch26 -p0
# FIXME:  deal with this
## put the configuration directory in an arch-specific location
#sed --in-place "s:/usr/lib/eclipse/configuration:%{_libdir}/%{name}/configuration:" library/eclipse.c
## make the eclipse binary relocatable
#sed --in-place "s:/usr/share/eclipse:%{_datadir}/%{name}:" library/eclipse.c
zip -q -9 -r ../../plugins/org.eclipse.platform/launchersrc.zip library
popd

# Use our system-installed javadocs, reference only what we built, and
# don't like to osgi.org docs (FIXME:  maybe we should package them?)
sed -i -e "s|http://java.sun.com/j2se/1.4.2/docs/api|%{_datadir}/javadoc/java|" \
   -e "/osgi\.org/d" \
   plugins/org.eclipse.platform.doc.isv/platformOptions.txt
sed -i -e "s|http://java.sun.com/j2se/1.5/docs/api|%{_datadir}/javadoc/java|" \
   -e "s/win32.win32.x86/gtk.linux.%{eclipse_arch}/" \
   plugins/org.eclipse.jdt.doc.isv/jdtaptOptions.txt \
   plugins/org.eclipse.jdt.doc.isv/jdtOptions.txt
sed -i -e "s|http://java.sun.com/j2se/1.4/docs/api|%{_datadir}/javadoc/java|" \
   -e "s/motif.linux.x86/gtk.linux.%{eclipse_arch}/" \
   plugins/org.eclipse.pde.doc.user/pdeOptions.txt \
   plugins/org.eclipse.pde.doc.user/pdeOptions

pushd plugins/org.eclipse.jdt.core
%patch14 -p0
%patch45 -p0
popd

pushd plugins/org.eclipse.pde.build
%patch15
sed --in-place "s:/usr/share/eclipse:%{_libdir}/%{name}:" templates/package-build/build.properties
popd

pushd features/org.eclipse.platform
# Move this file around due a bug in the metadata generator/parser that
# can't work with the compiler exclude
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=238240
cp -p gtk/eclipse.ini{,.orig}
%patch29
mv gtk/eclipse.ini{,.patched}
mv gtk/eclipse.ini{.orig,}
popd

#pushd plugins/org.eclipse.pde.api.tools
#%patch33
#popd
#pushd plugins/org.eclipse.pde.api.tools.ui
#%patch34
#popd

%patch36
%patch37

#pushd plugins/org.eclipse.equinox.p2.reconciler.dropins
#%patch39
#popd
#
#pushd plugins/org.eclipse.equinox.p2.touchpoint.eclipse
#%patch40
#popd

# Remove signatures for JARs
find -iname \*.sf | xargs rm
find -iname \*.rsa | xargs rm

# all output should be directed to stdout
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=144942
find -type f -name \*.xml -exec sed --in-place -r "s/output=\".*(txt|log).*\"//g" "{}" \;

# Remove existing .sos and binary launcher
find -name \*.so | xargs rm
find features/org.eclipse.equinox.executable -type f -name eclipse | xargs rm

# FIXME:  do this as part of Linux distros project
#
# the swt version is set to HEAD on s390x but shouldn't be
# get swt version
SWT_MAJ_VER=$(grep maj_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_MIN_VER=$(grep min_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_VERSION=$SWT_MAJ_VER$SWT_MIN_VER
swt_frag_ver=$(grep v$SWT_VERSION plugins/org.eclipse.swt.gtk.linux.x86/build.xml | sed "s:.*<.*\"\(.*\)\"/>:\1:")
swt_frag_ver_s390x=$(grep "version\.suffix\" value=" plugins/org.eclipse.swt.gtk.linux.s390x/build.xml | sed "s:.*<.*\"\(.*\)\"/>:\1:")
sed --in-place "s/$swt_frag_ver_s390x/$swt_frag_ver/g" plugins/org.eclipse.swt.gtk.linux.s390x/build.xml \
                                                      plugins/org.eclipse.swt.gtk.linux.s390x/META-INF/MANIFEST.MF \
                                                      plugins/org.eclipse.swt.gtk.linux.s390x.source/META-INF/MANIFEST.MF \
                                                      plugins/org.eclipse.swt.gtk.linux.s390x.source/build.xml \
                                                      assemble.org.eclipse.sdk.linux.gtk.s390x.xml \
						      features/org.eclipse.rcp/build.xml

# Nasty hack to get suppport for ppc64, sparc{,64} and alpha
%patch24 -p1
%patch28
%patch30
%patch31 -p1
%patch38

# replace ppc64 with a fake arch (ppc128) so we don't have duplicate ant targets
sed -i "s/\(rootFileslinux_gtk_\)ppc64/\1ppc128/g" \
  features/org.eclipse.equinox.executable/target.build.xml

# Copy all of the s390x directories and files to ppc64 or sparc{,64} or alpha dirs and replace
# the s390x strings with ppc64, etc.
%ifnarch %{ix86} x86_64
  cp -rp features/org.eclipse.platform/about_files/linux.gtk.{x86,%{_arch}}
%endif
%ifarch ppc64 sparc sparcv9 sparc64 alpha
  for f in $(find -name \*s390x\*); do
    tofile=$(echo $f | sed "s/s390x/%{_arch}/")
    cp -rp $f $tofile
    for g in $(find $tofile -type f); do
	sed -i "s/s390x/%{_arch}/g" $g
    done
  done
  OLDIFS=$IFS
IFS='
'
  for f in $(find -type f ! -name \*.java -a ! -name feature.xml -a ! -name \*.gif \
  -a ! -name \*.png -a ! -name \*.htm* -a ! -name \*.jar -a ! -name \
  \*.exe -a ! -name \*.pm -a ! -name \*.jpg -a ! -name \*win32\* | grep -v win32); do
   sed -i -e "s/s390x/%{_arch}/g" $f
  done
  IFS=$OLDIFS
%endif

%ifarch ppc64 sparc sparcv9 sparc64 alpha ia64
IFS='
'
 # Fragments for these arches
  rm -rf plugins/org.eclipse.equinox.launcher.gtk.linux.%{_arch}
  mv plugins/org.eclipse.equinox.launcher.gtk.linux.{ppc,%{_arch}}
  pushd plugins/org.eclipse.equinox.launcher.gtk.linux.%{_arch}
    for f in $(find -type f); do
      sed -i -e "s/ppc/%{_arch}/g" $f
      tofile=$(echo $f | sed "s/ppc/%{_arch}/")
      if [ $tofile != $f ]; then
        cp -rp $f $tofile
      fi
    done
  popd
  rm -rf plugins/org.eclipse.core.filesystem.linux.%{_arch}
  mv plugins/org.eclipse.core.filesystem.linux.{ppc,%{_arch}}
  pushd plugins/org.eclipse.core.filesystem.linux.%{_arch}
    for f in $(find -type f); do
      sed -i -e "s/ppc/%{_arch}/g" $f
      tofile=$(echo $f | sed "s/ppc/%{_arch}/")
      if [ $tofile != $f ]; then
        cp -rp $f $tofile
      fi
    done
  popd
  IFS=$OLDIFS

%endif

# Don't build for non-linux,gtk,%%{_arch} targets
pushd features
for f in */build.xml; do
    for platform in win32 macosx carbon hpux solaris aix qnx motif; do
      sed -i "/<ant antfile=\"build.xml\" dir=.*$platform.*target=\"/,/<\/ant>/ d" $f
      sed -i "/idReplacer/ s/org.eclipse\.\([a-z0-9A-Z_]\+\.\)\+$platform\(\.[a-z0-9A-Z_]\+\)*:0.0.0,[0-9\.Ivf\-]\+,//g" $f
    done
done
popd

arches=$(grep "antfile=\"build.xml\" dir=\".*gtk\.linux\.*" \
  features/org.eclipse.rcp/build.xml | awk '{ print $3 }' | awk -F . \
  '{ print $NF }' | sort -u | tr -d '"' | tr "\n" " ")

arches=$(echo $arches | sed s/%{eclipse_arch}//)

# Don't build for arches other than the one on which we're building
pushd features
for f in */build.xml; do
    for arch in $arches; do
      sed -i "/<ant antfile=\"build.xml\" dir=.*$arch\" target=\"/,/<\/ant>/ d" $f
      sed -i "/idReplacer/ s/org.eclipse\.\([a-z0-9A-Z_]\+\.\)\+$arch:0.0.0,[0-9I\.vf\-]\+,//g" $f
    done
done
popd

# Symlinks
rm plugins/org.sat4j*
ln -s %{_javadir}/org.sat4j.core* plugins/org.sat4j.core_2.0.3.v20081021.jar
ln -s %{_javadir}/org.sat4j.pb* plugins/org.sat4j.pb_2.0.3.v20081021.jar

ASMPLUGINVERSION=$(ls plugins | grep org.objectweb.asm_ | \
  sed 's/org.objectweb.asm_//')
rm plugins/org.objectweb.asm_$ASMPLUGINVERSION
ln -s %{_javadir}/asm3/asm-all.jar \
  plugins/org.objectweb.asm_$ASMPLUGINVERSION

## BEGIN ANT ##
ANTDIR=plugins/$(ls plugins | grep org.apache.ant_)
rm $ANTDIR/lib/*
ANTDIR=$ANTDIR/lib
ln -s %{_javadir}/ant/ant-antlr.jar $ANTDIR/ant-antlr.jar
ln -s %{_javadir}/ant/ant-apache-bcel.jar $ANTDIR/ant-apache-bcel.jar
ln -s %{_javadir}/ant/ant-apache-bsf.jar $ANTDIR/ant-apache-bsf.jar
ln -s %{_javadir}/ant/ant-apache-log4j.jar $ANTDIR/ant-apache-log4j.jar
ln -s %{_javadir}/ant/ant-apache-oro.jar $ANTDIR/ant-apache-oro.jar
ln -s %{_javadir}/ant/ant-apache-regexp.jar $ANTDIR/ant-apache-regexp.jar
ln -s %{_javadir}/ant/ant-apache-resolver.jar $ANTDIR/ant-apache-resolver.jar
ln -s %{_javadir}/ant/ant-commons-logging.jar $ANTDIR/ant-commons-logging.jar
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=180642
# the symlinks that are commented-out are not currently shipped on Fedora
ln -s %{_javadir}/ant/ant-commons-net.jar $ANTDIR/ant-commons-net.jar
#ln -s %{_javadir}/ant/ant-jai.jar $ANTDIR/ant-jai.jar
ln -s %{_javadir}/ant.jar $ANTDIR/ant.jar
ln -s %{_javadir}/ant/ant-javamail.jar $ANTDIR/ant-javamail.jar
ln -s %{_javadir}/ant/ant-jdepend.jar $ANTDIR/ant-jdepend.jar
#ln -s %{_javadir}/ant/ant-jmf.jar $ANTDIR/ant-jmf.jar
ln -s %{_javadir}/ant/ant-jsch.jar $ANTDIR/ant-jsch.jar
ln -s %{_javadir}/ant/ant-junit.jar $ANTDIR/ant-junit.jar
ln -s %{_javadir}/ant-launcher.jar $ANTDIR/ant-launcher.jar
#ln -s %{_javadir}/ant/ant-netrexx.jar $ANTDIR/ant-netrexx.jar
ln -s %{_javadir}/ant/ant-nodeps.jar $ANTDIR/ant-nodeps.jar
#ln -s %{_javadir}/ant/ant-starteam.jar $ANTDIR/ant-starteam.jar
#ln -s %{_javadir}/ant/ant-stylebook.jar $ANTDIR/ant-stylebook.jar
ln -s %{_javadir}/ant/ant-swing.jar $ANTDIR/ant-swing.jar
ln -s %{_javadir}/ant/ant-trax.jar $ANTDIR/ant-trax.jar
#ln -s %{_javadir}/ant/ant-weblogic.jar $ANTDIR/ant-weblogic.jar
## END ANT ##

JETTYPLUGINVERSION=$(ls plugins | grep org.mortbay.jetty_5 | sed 's/org.mortbay.jetty_//')
rm plugins/org.mortbay.jetty_$JETTYPLUGINVERSION
ln -s %{_javadir}/jetty5/jetty5.jar plugins/org.mortbay.jetty_$JETTYPLUGINVERSION

JUNITVERSION=$(ls plugins | grep org.junit_3 | sed 's/org.junit_//')
build-jar-repository -s -p plugins/org.junit_$JUNITVERSION junit

rm plugins/org.junit4/junit.jar
ln -s %{_javadir}/junit4.jar plugins/org.junit4/junit.jar

# link to the jsch jar
JSCHVERSION=$(ls plugins | grep com.jcraft.jsch_ | \
  sed 's/com.jcraft.jsch_//')
rm plugins/com.jcraft.jsch_*.jar
ln -s %{_javadir}/jsch.jar plugins/com.jcraft.jsch_$JSCHVERSION

# link to the icu4j stuff
ICUVERSION=$(ls plugins | grep com.ibm.icu_ | sed 's/com.ibm.icu_//')
rm plugins/com.ibm.icu_*.jar
ln -s %{_libdir}/eclipse/plugins/com.ibm.icu_*.jar plugins/com.ibm.icu_$ICUVERSION

# link to lucene
LUCENEVERSION=$(ls plugins | grep org.apache.lucene_ | \
  sed 's/org.apache.lucene_//')
rm plugins/org.apache.lucene_*
ln -s %{_javadir}/lucene.jar plugins/org.apache.lucene_$LUCENEVERSION
rm plugins/org.apache.lucene.analysis_*
ln -s %{_javadir}/lucene-contrib/lucene-analyzers.jar \
  plugins/org.apache.lucene.analysis_$LUCENEVERSION

# link to commons-logging
COMMONSLOGGINGVERSION=$(ls plugins | grep commons.logging_ | \
  sed 's/org.apache.commons.logging_//')
rm plugins/org.apache.commons.logging_$COMMONSLOGGINGVERSION
ln -s %{_javadir}/commons-logging.jar \
  plugins/org.apache.commons.logging_$COMMONSLOGGINGVERSION

# link to commons-el
COMMONSELVERSION=$(ls plugins | grep commons.el_ | \
  sed 's/org.apache.commons.el_//')
rm plugins/org.apache.commons.el_$COMMONSELVERSION
ln -s %{_javadir}/commons-el.jar \
  plugins/org.apache.commons.el_$COMMONSELVERSION

# link to jasper
JASPERVERSION=$(ls plugins | grep org.apache.jasper_ | \
  sed 's/org.apache.jasper_//')
rm plugins/org.apache.jasper_*.jar
ln -s %{_datadir}/eclipse/plugins/org.apache.jasper_* \
   plugins/org.apache.jasper_$JASPERVERSION

# link to servlet-api
SERVLETAPIVERSION=$(ls plugins | grep javax.servlet_ | \
  sed 's/javax.servlet_//')
rm plugins/javax.servlet_*
ln -s %{_javadir}/tomcat5-servlet-2.4-api.jar \
  plugins/javax.servlet_$SERVLETAPIVERSION

# link to jsp-api
JSPAPIVERSION=$(ls plugins | grep javax.servlet.jsp_ | \
  sed 's/javax.servlet.jsp_//')
rm plugins/javax.servlet.jsp_*
ln -s %{_javadir}/tomcat5-jsp-2.0-api.jar \
  plugins/javax.servlet.jsp_$JSPAPIVERSION

# delete included jars
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=170662
rm plugins/org.eclipse.swt.win32.win32.x86/swt.jar \
   plugins/org.eclipse.swt/extra_jars/exceptions.jar \
   plugins/org.eclipse.swt.tools/swttools.jar \
   plugins/org.eclipse.osgi/osgi/osgi.cmpn.jar \
   plugins/org.eclipse.osgi/osgi/osgi.core.jar \
   plugins/org.eclipse.osgi/supplement/osgi/osgi.jar

# FIXME:  figure out a way to symlink to something.  Alternatively,
# patch out of package.org.eclipse.sdk*.xml.
# Delete unnecessary-for-build source JARs
#rm plugins/*.source_*.jar

# make sure there are no jars left
JARS=""
for j in $(find -name \*.jar); do
  if [ ! -L $j ]; then
    JARS="$JARS `echo $j`"
  fi
done
if [ ! -z "$JARS" ]; then
    echo "These jars should be deleted and symlinked to system jars: $JARS"
   #FIXME: enable  exit 1
fi

tar jxf %{SOURCE20}

# ECF filetransfer plugins
tar jxf %{SOURCE25}
pushd org.eclipse.ecf
%patch35
mkdir -p features/org.eclipse.ecf.filetransfer-feature
pushd features/org.eclipse.ecf.filetransfer-feature
cp -p %{SOURCE26} feature.xml
cp -p %{SOURCE27} build.properties
popd
popd
sed --in-place "s/uname \-p/uname \-m/"  plugins/org.eclipse.swt/Eclipse\ SWT\ PI/gtk/library/build.sh

# Test framework
tar jxvf %{SOURCE30}
pushd %{name}-%{version}-testframework
%patch41
pushd org.eclipse.test
%patch42
popd
sed -i "s:/usr/lib/eclipse:%{_libdir}/%{name}:" org.eclipse.test/library.xml
popd

%patch43
%patch44
%patch46 -p1

%build
ORIGCLASSPATH=$CLASSPATH

# Bootstrapping:
# 1. Build ecj with javac
%ant -DcompilerArg="-encoding ISO-8859-1 -nowarn" -buildfile jdtcoresrc/compilejdtcorewithjavac.xml

# 2. Use this ecj to rebuild itself
export CLASSPATH=`pwd`/jdtcoresrc/ecj.jar:$ORIGCLASSPATH
%ant -DcompilerArg="-encoding ISO-8859-1 -nowarn" -buildfile jdtcoresrc/compilejdtcore.xml

# Build the rest of Eclipse
export CLASSPATH=`pwd`/ecj.jar:$ORIGCLASSPATH
export JAVA_HOME=%{java_home}
%ant \
  -Dnobootstrap=true \
  -DinstallOs=linux -DinstallWs=gtk -DinstallArch=%{eclipse_arch} \
  -Dlibsconfig=true \
  -DJavaSE-1.6=%{_jvmdir}/java/jre/lib/rt.jar \
  -DcompilerArg="-encoding ISO-8859-1 -nowarn"

# Build the FileInitializer application
SDK=$(cd eclipse && pwd)
mkdir -p home
homedir=$(cd home && pwd)
LAUNCHERVERSION=$(ls $SDK/plugins | grep equinox.launcher_ | sed 's/org.eclipse.equinox.launcher_//')
PDEPLUGINVERSION=$(ls $SDK/plugins | grep pde.build_ | sed 's/org.eclipse.pde.build_//')
pushd equinox-incubator
mkdir -p build

# This can go away when package build handles plugins (not just features)
echo "<project default=\"main\"><target name=\"main\"></target></project>" > build/assemble.org.eclipse.equinox.initializer.all.xml
echo "<project default=\"main\"><target name=\"main\"></target></project>" > build/package.org.eclipse.equinox.initializer.all.xml

%java -cp $SDK/plugins/org.eclipse.equinox.launcher_$LAUNCHERVERSION \
     -Duser.home=$homedir                              \
      org.eclipse.core.launcher.Main \
     -application org.eclipse.ant.core.antRunner       \
     -Dtype=plugin                                    \
     -Did=org.eclipse.equinox.initializer                   \
     -DsourceDirectory=$(pwd)                          \
     -DbaseLocation=$SDK \
     -Dbuilder=$SDK/plugins/org.eclipse.pde.build_$PDEPLUGINVERSION/templates/package-build  \
     -f $SDK/plugins/org.eclipse.pde.build_$PDEPLUGINVERSION/scripts/build.xml

pushd build/plugins/org.eclipse.equinox.initializer
%java -cp $SDK/plugins/org.eclipse.equinox.launcher_$LAUNCHERVERSION \
     -Duser.home=$homedir                              \
      org.eclipse.core.launcher.Main \
     -application org.eclipse.ant.core.antRunner       \
     -f build.xml build.update.jar
popd
popd

# Build the ECF filetransfer plugins
pushd org.eclipse.ecf
mkdir -p build

%java -cp $SDK/plugins/org.eclipse.equinox.launcher_$LAUNCHERVERSION \
     -Duser.home=$homedir                              \
      org.eclipse.core.launcher.Main \
     -application org.eclipse.ant.core.antRunner       \
     -Dtype=feature                                    \
     -Did=org.eclipse.ecf.filetransfer_feature                   \
     -DsourceDirectory=$(pwd)                          \
     -DbaseLocation=$SDK \
     -Dbuilder=$SDK/plugins/org.eclipse.pde.build_$PDEPLUGINVERSION/templates/package-build  \
     -f $SDK/plugins/org.eclipse.pde.build_$PDEPLUGINVERSION/scripts/build.xml

popd

# Build the test framework
pushd %{name}-%{version}-testframework
mkdir -p build

# The qualifier is what is in upstream's release:
# http://download.eclipse.org/eclipse/downloads/drops/R-3.4-200806172000/eclipse-test-framework-3.4.zip
%java -cp $SDK/plugins/org.eclipse.equinox.launcher_$LAUNCHERVERSION \
     -Duser.home=$homedir                              \
      org.eclipse.core.launcher.Main \
     -application org.eclipse.ant.core.antRunner       \
     -Dtype=feature                                    \
     -Did=org.eclipse.test                   \
     -DsourceDirectory=$(pwd)                          \
     -DbaseLocation=$SDK \
     -DforceContextQualifier=v20080507 \
     -Dbuilder=$SDK/plugins/org.eclipse.pde.build_$PDEPLUGINVERSION/templates/package-build  \
     -f $SDK/plugins/org.eclipse.pde.build_$PDEPLUGINVERSION/scripts/build.xml

unzip build/rpmBuild/org.eclipse.test.zip
# These are already in the SDK
rm eclipse/epl-v10.html eclipse/notice.html
rm -rf eclipse/plugins/org.junit*
rm build/rpmBuild/org.eclipse.test.zip
zip -r build/rpmBuild/org.eclipse.test.zip eclipse
popd


%install
# Get swt version
SWT_MAJ_VER=$(grep maj_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_MIN_VER=$(grep min_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_VERSION=$SWT_MAJ_VER$SWT_MIN_VER

# Some directories we need
sdkDir=$RPM_BUILD_ROOT%{_libdir}/%{name}
install -d -m 755 $sdkDir
install -d -m 755 $sdkDir/plugins
install -d -m 755 $sdkDir/features
# FIXME:  We can probably get rid of the links directory (for the
# datadir.link file) when we ensure all plugins are installing into
# dropins (either in libdir or datadir).
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/java
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/dropins

# FIXME:  Please don't install stuff to these directories.  They're only
# still here for legacy plugins (which probably won't function in 3.4).
# We'll remove these later.
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/features
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins

# Explode the resulting SDK tarball
tar -C $RPM_BUILD_ROOT%{_libdir} -zxf result/linux-gtk-%{eclipse_arch}-sdk.tar.gz

# ECF filetransfer plugins we built
rm $sdkDir/plugins/org.eclipse.ecf*.jar
unzip -d $RPM_BUILD_ROOT%{_libdir} \
  org.eclipse.ecf/build/rpmBuild/org.eclipse.ecf.filetransfer_feature.zip
# Remove the feature we used for building
rm -rf \
  $sdkDir/features/org.eclipse.ecf.filetransfer_feature_*

# Test framework
unzip -d $RPM_BUILD_ROOT%{_libdir} \
  %{name}-%{version}-testframework/build/rpmBuild/org.eclipse.test.zip
mv $RPM_BUILD_ROOT%{_libdir}/eclipse/plugins/org.eclipse.test{_3.2.0,}

LAUNCHERVERSION=$(ls $sdkDir/plugins | grep equinox.launcher_ | sed 's/org.eclipse.equinox.launcher_//')

# Install the file initializer app
cp -p equinox-incubator/org.eclipse.equinox.initializer/org.eclipse.equinox.initializer_*.jar \
  $sdkDir/plugins

# Install the Mandriva Eclipse product plugin
unzip -qq -d $sdkDir/plugins %{SOURCE4}
# Install the Mandriva Eclipse product feature
unzip -qq -d $sdkDir/features %{SOURCE5}

installDir=$sdkDir-Platform
metadataDir=$installDir/metadata-Platform
provisionDir=$installDir-provisioned
profileId=PlatformProfile

# Copy just the platform
mkdir $installDir
pushd $installDir
sh %{SOURCE28} $sdkDir
mv plugins/*.source* $sdkDir/plugins
popd

# Generate metadata for the platform
%java \
-cp $installDir/plugins/org.eclipse.equinox.launcher_$LAUNCHERVERSION \
org.eclipse.core.launcher.Main \
-application \
org.eclipse.equinox.p2.metadata.generator.EclipseGenerator \
-metadataRepository file:$metadataDir \
-artifactRepository file:$metadataDir \
-source $installDir \
-root "Mandriva Eclipse Platform" \
-rootVersion %{version} \
-flavor tooling \
-publishArtifacts \
-append \
-artifactRepositoryName "Mandriva Eclipse" \
-metadataRepositoryName "Mandriva Eclipse"

# JDT
jdtDir=$sdkDir-JDT
jdtMetadata=$jdtDir/metadata-JDT

mkdir $jdtDir
pushd $jdtDir
mkdir features plugins
mv $sdkDir/features/org.eclipse.jdt_* features
for plugin in org.eclipse.jdt \
  org.eclipse.ant.ui \
  org.eclipse.jdt.apt.core \
  org.eclipse.jdt.apt.ui \
  org.eclipse.jdt.apt.pluggable.core \
  org.eclipse.jdt.compiler.apt \
  org.eclipse.jdt.compiler.tool \
  org.eclipse.jdt.core \
  org.eclipse.jdt.core.manipulation \
  org.eclipse.jdt.debug.ui \
  org.eclipse.jdt.debug \
  org.eclipse.jdt.junit \
  org.eclipse.jdt.junit.runtime \
  org.eclipse.jdt.junit4.runtime \
  org.eclipse.jdt.launching \
  org.eclipse.jdt.ui \
  org.junit \
  org.junit4 \
  org.eclipse.jdt.doc.user; do
  mv $sdkDir/plugins/${plugin}_* plugins
done
popd

# Generate metadata for JDT
%java \
-cp $installDir/plugins/org.eclipse.equinox.launcher_$LAUNCHERVERSION \
org.eclipse.core.launcher.Main \
-application \
org.eclipse.equinox.p2.metadata.generator.EclipseGenerator \
-metadataRepository file:$jdtMetadata \
-artifactRepository file:$jdtMetadata \
-source $jdtDir \
-root "Mandriva Eclipse JDT" \
-rootVersion %{version} \
-flavor tooling \
-append \
-artifactRepositoryName "Mandriva Eclipse" \
-metadataRepositoryName "Mandriva Eclipse"

# SDK
sdkMetadata=$sdkDir/metadata-SDK

# Generate metadata for SDK
%java \
-cp $installDir/plugins/org.eclipse.equinox.launcher_$LAUNCHERVERSION \
org.eclipse.core.launcher.Main \
-application \
org.eclipse.equinox.p2.metadata.generator.EclipseGenerator \
-metadataRepository file:$sdkMetadata \
-artifactRepository file:$sdkMetadata \
-source $sdkDir \
-root "Mandriva Eclipse SDK" \
-rootVersion %{version} \
-flavor tooling \
-publishArtifacts \
-append \
-artifactRepositoryName "Mandriva Eclipse" \
-metadataRepositoryName "Mandriva Eclipse"

# Director config.ini
mv $installDir/configuration/config.ini{,.bak}
cp -p %{SOURCE22} $installDir/configuration/config.ini

# Debugging?  Add -debug and -consolelog
# Provision with director
%java \
-Declipse.p2.data.area=file://$provisionDir/p2 \
-cp $installDir/plugins/org.eclipse.equinox.launcher_$LAUNCHERVERSION \
org.eclipse.core.launcher.Main \
-application \
org.eclipse.equinox.p2.director.app.application \
-flavor tooling \
-installIU "Mandriva Eclipse Platform" \
-version %{version} \
-p2.os linux \
-p2.ws gtk \
-p2.arch %{eclipse_arch} \
-roaming \
-profile $profileId \
-profileProperties org.eclipse.update.install.features=true \
-metadataRepository file:$metadataDir \
-artifactRepository file:$metadataDir \
-destination $provisionDir \
-bundlepool $provisionDir

# Stuff in JDT, PDE, SDK
for f in about.html about_files \.eclipseproduct epl-v10.html notice.html readme; do
    if 	[ -e $installDir/$f ]; then
      mv $installDir/$f $provisionDir
    fi
done
# FIXME:  should add artifacts.xml here
dropins=$provisionDir/dropins
mkdir -p $dropins/jdt $dropins/sdk
mv $jdtDir/features $dropins/jdt
mv $jdtDir/plugins $dropins/jdt
mv $jdtMetadata/content.xml $dropins/jdt

mv $sdkDir/features $dropins/sdk
mv $sdkDir/plugins $dropins/sdk

mv $sdkMetadata/content.xml $dropins/sdk
rm -rf $metadataDir $jdtDir $sdkDir $installDir
mv $provisionDir $sdkDir

# Fix paths in p2 data
rm -rf $sdkDir/p2/org.eclipse.equinox.p2.core/cache
rm -rf $sdkDir/p2/org.eclipse.equinox.p2.director/rollback/content.xml
sed -i "s|file\:$provisionDir/\ -\ bundle\ pool|Mandriva Eclipse|g" \
  $sdkDir/artifacts.xml
profileDir=$sdkDir/p2/org.eclipse.equinox.p2.engine/profileRegistry
pushd $profileDir
  sed -i "s|$provisionDir|%{_libdir}/%{name}|g" \
    PlatformProfile.profile/*
  sed -i "s|$RPM_BUILD_ROOT||g" PlatformProfile.profile/*
popd

%ifarch ppc64 sparc sparcv9 sparc64 alpha ia64
cp -p features/org.eclipse.platform/gtk/eclipse.ini $sdkDir
%endif

cp -p features/org.eclipse.platform/gtk/eclipse.ini.patched \
  $sdkDir/eclipse.ini
# We have /usr/share/eclipse/dropins in eclipse.ini
sed -i "s|/usr/share|%{_datadir}|" $sdkDir/eclipse.ini

# Add a compatibility symlink to startup.jar
pushd $sdkDir
LAUNCHERNAME=$(ls plugins | grep equinox.launcher_)
ln -s plugins/$LAUNCHERNAME startup.jar
popd

# FIXME: investigate why it doesn't work to set this -- configuration data is
# always written to /usr/share/eclipse/configuration, even with
#     -Dosgi.sharedConfiguration.area=$RPM_BUILD_ROOT%{_libdir}/%{name}/configuration
# Note (2006-12-05):  upon looking at this again, we (bkonrath, overholt) don't
# know what we're doing with $libdir_path :)  It requires some investigation.
#
# Extract .so files
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=90535
pushd $RPM_BUILD_ROOT
libdir_path=$(echo %{_libdir}/%{name} | sed -e 's/^\///')
%java -Dosgi.sharedConfiguration.area=$libdir_path/configuration \
     -cp $libdir_path/startup.jar \
     org.eclipse.core.launcher.Main \
     -consolelog \
     -application org.eclipse.equinox.initializer.configInitializer \
     -fileInitializer %{SOURCE19}
popd

# Remove the unnecessary configuration data
rm -r $sdkDir/configuration/org.eclipse.update
rm -r $sdkDir/configuration/org.eclipse.core.runtime
rm -r $sdkDir/configuration/org.eclipse.equinox.app
rm -r $sdkDir/configuration/.settings
rm -rf $sdkDir/configuration/*.log
dataDirs=$(find $sdkDir/configuration \
  -type d -name data)
for dataDir in $dataDirs; do
    rm -rf `dirname $dataDir`
done

# Do this again after we've run the file initializer
rm -rf $sdkDir/p2/org.eclipse.equinox.p2.core/cache
rm -rf $sdkDir/p2/org.eclipse.equinox.p2.director/rollback/content.xml
pushd $profileDir
  sed -i "s|$RPM_BUILD_ROOT||g" *.profile/*
popd

pushd $sdkDir
# Create file listings for the extracted shared libraries
echo -n "" > %{_builddir}/%{name}-%{version}/%{name}-platform.install;
echo -n "" > %{_builddir}/%{name}-%{version}/%{name}-swt.install;
for id in `ls configuration/org.eclipse.osgi/bundles`; do
  if [ "Xconfiguration" = $(echo X`find configuration/org.eclipse.osgi/bundles/$id -name libswt\*.so` | sed "s:/.*::") ]; then
    echo "%{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles/$id" > %{_builddir}/%{name}-%{version}/%{name}-swt.install;
  else
    echo "%{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles/$id" >> %{_builddir}/%{name}-%{version}/%{name}-platform.install;
  fi
done
popd

# Install symlinks to the SWT JNI shared libraries in %%{_libdir}/eclipse
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
for lib in $(find configuration -name libswt\*.so); do
  rm -f `basename $lib`
  ln -sf $lib `basename $lib`
done
popd

# Set eclipse.product to org.mandriva.ide.platform
sed --in-place "s/plugins\/org.eclipse.platform/plugins\/org.mandriva.ide.platform/" \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/configuration/config.ini
sed --in-place "s/eclipse.product=org.eclipse.platform.ide/eclipse.product=org.mandriva.ide.platform.product/" \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/configuration/config.ini

# Install the Eclipse binary wrapper
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
ln -s %{_libdir}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
#install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
#cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/eclipse
#sed --in-place "s|@LIBDIR@|%{_libdir}|g" $RPM_BUILD_ROOT%{_bindir}/eclipse
#ECLIPSELIBSUFFIX=$(ls $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/org.eclipse.equinox.launcher.gtk.linux*/*.so | sed "s/.*.launcher.gtk.linux.//")
#sed --in-place "s|@ECLIPSELIBSUFFIX@|$ECLIPSELIBSUFFIX|" $RPM_BUILD_ROOT%{_bindir}/eclipse

# Ensure the shared libraries have the correct permissions
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
for lib in `find configuration -name \*.so`; do
   chmod 755 $lib
done

mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/links
# FIXME:  We can probably get rid of the links file when we ensure all
# plugins are installing into dropins (either in libdir or datadir).
# Set up an extension location and a link file for the arch-independent dir
echo "path:%{_datadir}" > \
  $sdkDir/links/datadir.link

# Ensure the launcher binary has the correct permissions
chmod 755 $RPM_BUILD_ROOT/%{_libdir}/%{name}/%{name}

# Create file listings for the extracted shared libraries
echo -n "" > %{_builddir}/%{buildsubdir}/%{name}-platform.install;
for id in `ls configuration/org.eclipse.osgi/bundles`; do
  if [ "Xconfiguration" = $(echo X`find configuration/org.eclipse.osgi/bundles/$id -name libswt\*.so` | sed "s:/.*::") ]; then
    echo "%{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles/$id" > %{_builddir}/%{buildsubdir}/%{name}-swt.install;
  else
    echo "%{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles/$id" >> %{_builddir}/%{buildsubdir}/%{name}-platform.install;
  fi
done
popd

# Install symlinks to the SWT JNI shared libraries in %%{_libdir}/eclipse
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
for lib in $(find configuration -name libswt\*.so); do
  rm -f `basename $lib`
  ln -sf $lib `basename $lib`
done
popd

# Install the SWT jar symlinks in libdir
SWTJARVERSION=$(grep v$SWT_VERSION plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}/build.xml | sed "s:.*<.*\"\(.*\)\"/>:\1:")
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
ln -s plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}_$SWTJARVERSION.jar swt-gtk-%{eclipse_majmin}.%{eclipse_micro}.jar
ln -s swt-gtk-%{eclipse_majmin}.%{eclipse_micro}.jar swt-gtk-%{eclipse_majmin}.jar
ln -s swt-gtk-%{eclipse_majmin}.%{eclipse_micro}.jar swt.jar
mkdir -p %{buildroot}%{_jnidir}
ln -s %{_libdir}/%{name}/swt-gtk-%{eclipse_majmin}.%{eclipse_micro}.jar %{buildroot}%{_jnidir}/swt.jar
popd

# Install the eclipse-ecj.jar symlink for java-1.4.2-gcj-compat's "javac"
JDTCORESUFFIX=$(ls $RPM_BUILD_ROOT%{_libdir}/%{name}/dropins/jdt/plugins \
  | grep jdt.core_ | sed "s/org.eclipse.jdt.core_//")
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
ln -s %{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.core_$JDTCORESUFFIX \
  $RPM_BUILD_ROOT%{_javadir}/eclipse-ecj-%{version}.jar
ln -s %{_javadir}/eclipse-ecj-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/eclipse-ecj.jar
ln -s %{_javadir}/eclipse-ecj-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/jdtcore-%{version}.jar
ln -s %{_javadir}/jdtcore-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/jdtcore.jar
ln -s %{_javadir}/eclipse-ecj-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/ecj-%{version}.jar
ln -s %{_javadir}/ecj-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/ecj.jar

# Icons
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
ln -s %{_libdir}/%{name}/plugins/org.mandriva.ide.platform_%{version}/eclipse48.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
ln -s %{_libdir}/%{name}/plugins/org.mandriva.ide.platform_%{version}/eclipse32.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
ln -s %{_libdir}/%{name}/plugins/org.mandriva.ide.platform_%{version}/eclipse.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pixmaps
ln -s %{_datadir}/icons/hicolor/48x48/apps/%{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps

# Install the efj wrapper script
install -p -D -m0755 %{SOURCE17} $RPM_BUILD_ROOT%{_bindir}/efj
sed --in-place "s:startup.jar:%{_libdir}/%{name}/startup.jar:" \
  $RPM_BUILD_ROOT%{_bindir}/efj

# Install the ecj wrapper script
install -p -D -m0755 %{SOURCE18} $RPM_BUILD_ROOT%{_bindir}/ecj
sed --in-place "s:@JAVADIR@:%{_javadir}:" $RPM_BUILD_ROOT%{_bindir}/ecj

# A sanity check.
desktop-file-validate %{SOURCE2}

# freedesktop.org menu entry
install -p -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Create a script that can be used to make a symlink tree of the
# eclipse platform.
cp -p %{SOURCE16} copy-platform
(
  cd $RPM_BUILD_ROOT%{_libdir}/%{name}
  ls -d * | egrep -v '^(plugins|features|about_files|dropins)$'
  ls -d plugins/* features/*
) |
sed -e's,^\(.*\),[ ! -e \1 ] \&\& ln -s $eclipse/\1 \1,' >> copy-platform
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts
cp -p copy-platform $RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts
copyPlatform=$RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts/copy-platform
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
for p in $(ls -d dropins/jdt/plugins/*); do
    plugin=$(basename $p)
    echo $p | sed -e"s,^\(.*\),[ ! -e plugins/$plugin ] \&\& ln -s \$eclipse/\1 plugins/$plugin," >> $copyPlatform
done
for p in $(ls -d dropins/sdk/plugins/*); do
    plugin=$(basename $p)
    echo $p | sed -e"s,^\(.*\),[ ! -e plugins/$plugin ] \&\& ln -s \$eclipse/\1 plugins/$plugin," >> $copyPlatform
done
popd

# Install the PDE Build wrapper script.
install -p -D -m0755 %{SOURCE21} \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts/pdebuild
PDEBUILDVERSION=$(ls $RPM_BUILD_ROOT%{_libdir}/%{name}/dropins/sdk/plugins \
  | grep org.eclipse.pde.build_ | \
  sed 's/org.eclipse.pde.build_//')
sed -i "s/@PDEBUILDVERSION@/$PDEBUILDVERSION/g" \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts/pdebuild

pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
rm plugins/org.sat4j*
ln -s %{_javadir}/org.sat4j.core* plugins/org.sat4j.core_2.0.3.v20081021.jar
ln -s %{_javadir}/org.sat4j.pb* plugins/org.sat4j.pb_2.0.3.v20081021.jar

ASMPLUGINVERSION=$(ls dropins/sdk/plugins | grep org.objectweb.asm_ | \
  sed 's/org.objectweb.asm_//')
rm dropins/sdk/plugins/org.objectweb.asm_$ASMPLUGINVERSION
ln -s %{_javadir}/asm3/asm-all.jar \
  dropins/sdk/plugins/org.objectweb.asm_$ASMPLUGINVERSION

## BEGIN ANT ##
ANTDIR=plugins/$(ls plugins | grep org.apache.ant_)
rm $ANTDIR/lib/*
ANTDIR=$ANTDIR/lib
ln -s %{_javadir}/ant/ant-antlr.jar $ANTDIR/ant-antlr.jar
ln -s %{_javadir}/ant/ant-apache-bcel.jar $ANTDIR/ant-apache-bcel.jar
ln -s %{_javadir}/ant/ant-apache-bsf.jar $ANTDIR/ant-apache-bsf.jar
ln -s %{_javadir}/ant/ant-apache-log4j.jar $ANTDIR/ant-apache-log4j.jar
ln -s %{_javadir}/ant/ant-apache-oro.jar $ANTDIR/ant-apache-oro.jar
ln -s %{_javadir}/ant/ant-apache-regexp.jar $ANTDIR/ant-apache-regexp.jar
ln -s %{_javadir}/ant/ant-apache-resolver.jar $ANTDIR/ant-apache-resolver.jar
ln -s %{_javadir}/ant/ant-commons-logging.jar $ANTDIR/ant-commons-logging.jar
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=180642
# the symlinks that are commented-out are not currently shipped on Fedora
ln -s %{_javadir}/ant/ant-commons-net.jar $ANTDIR/ant-commons-net.jar
#ln -s %{_javadir}/ant/ant-jai.jar $ANTDIR/ant-jai.jar
ln -s %{_javadir}/ant.jar $ANTDIR/ant.jar
ln -s %{_javadir}/ant/ant-javamail.jar $ANTDIR/ant-javamail.jar
ln -s %{_javadir}/ant/ant-jdepend.jar $ANTDIR/ant-jdepend.jar
#ln -s %{_javadir}/ant/ant-jmf.jar $ANTDIR/ant-jmf.jar
ln -s %{_javadir}/ant/ant-jsch.jar $ANTDIR/ant-jsch.jar
ln -s %{_javadir}/ant/ant-junit.jar $ANTDIR/ant-junit.jar
ln -s %{_javadir}/ant-launcher.jar $ANTDIR/ant-launcher.jar
#ln -s %{_javadir}/ant/ant-netrexx.jar $ANTDIR/ant-netrexx.jar
ln -s %{_javadir}/ant/ant-nodeps.jar $ANTDIR/ant-nodeps.jar
#ln -s %{_javadir}/ant/ant-starteam.jar $ANTDIR/ant-starteam.jar
#ln -s %{_javadir}/ant/ant-stylebook.jar $ANTDIR/ant-stylebook.jar
ln -s %{_javadir}/ant/ant-swing.jar $ANTDIR/ant-swing.jar
ln -s %{_javadir}/ant/ant-trax.jar $ANTDIR/ant-trax.jar
#ln -s %{_javadir}/ant/ant-weblogic.jar $ANTDIR/ant-weblogic.jar
## END ANT ##

JETTYPLUGINVERSION=$(ls plugins | grep org.mortbay.jetty_5 | sed 's/org.mortbay.jetty_//')
rm plugins/org.mortbay.jetty_$JETTYPLUGINVERSION
ln -s %{_javadir}/jetty5/jetty5.jar plugins/org.mortbay.jetty_$JETTYPLUGINVERSION

pushd dropins/jdt
build-jar-repository -s -p plugins/org.junit_* junit

JUNIT4VERSION=$(ls plugins | grep org.junit4_ | sed 's/org.junit4_//')
rm plugins/org.junit4_$JUNIT4VERSION/junit.jar
ln -s %{_javadir}/junit4.jar plugins/org.junit4_$JUNIT4VERSION/junit.jar
popd

JSCHVERSION=$(ls plugins | grep com.jcraft.jsch_ | sed 's/com.jcraft.jsch_//')
rm plugins/com.jcraft.jsch_$JSCHVERSION
ln -s %{_javadir}/jsch.jar plugins/com.jcraft.jsch_$JSCHVERSION

# link to the icu4j stuff
ICUVERSION=$(ls plugins | grep com.ibm.icu_ | sed 's/com.ibm.icu_//')
rm plugins/com.ibm.icu_*.jar
ln -s %{_libdir}/eclipse/plugins/com.ibm.icu_*.jar plugins/com.ibm.icu_$ICUVERSION

# link to lucene
LUCENEVERSION=$(ls plugins | grep org.apache.lucene_ | \
  sed 's/org.apache.lucene_//')
rm plugins/org.apache.lucene_*
ln -s %{_javadir}/lucene.jar plugins/org.apache.lucene_$LUCENEVERSION
rm plugins/org.apache.lucene.analysis_*
ln -s %{_javadir}/lucene-contrib/lucene-analyzers.jar \
  plugins/org.apache.lucene.analysis_$LUCENEVERSION

# link to commons-logging
COMMONSLOGGINGVERSION=$(ls plugins | grep commons.logging_ | \
  sed 's/org.apache.commons.logging_//')
rm plugins/org.apache.commons.logging_$COMMONSLOGGINGVERSION
ln -s %{_javadir}/commons-logging.jar \
  plugins/org.apache.commons.logging_$COMMONSLOGGINGVERSION

# link to commons-el
COMMONSELVERSION=$(ls plugins | grep commons.el_ | \
  sed 's/org.apache.commons.el_//')
rm plugins/org.apache.commons.el_$COMMONSELVERSION
ln -s %{_javadir}/commons-el.jar \
  plugins/org.apache.commons.el_$COMMONSELVERSION

# link to jasper
JASPERVERSION=$(ls plugins | grep org.apache.jasper_ | \
  sed 's/org.apache.jasper_//')
rm plugins/org.apache.jasper_*.jar
ln -s %{_datadir}/eclipse/plugins/org.apache.jasper_* \
   plugins/org.apache.jasper_$JASPERVERSION

# link to servlet-api
SERVLETAPIVERSION=$(ls plugins | grep javax.servlet_ | \
  sed 's/javax.servlet_//')
rm plugins/javax.servlet_*
ln -s %{_javadir}/tomcat5-servlet-2.4-api.jar \
  plugins/javax.servlet_$SERVLETAPIVERSION

# link to jsp-api
JSPAPIVERSION=$(ls plugins | grep javax.servlet.jsp_ | \
  sed 's/javax.servlet.jsp_//')
rm plugins/javax.servlet.jsp_*
ln -s %{_javadir}/tomcat5-jsp-2.0-api.jar \
  plugins/javax.servlet.jsp_$JSPAPIVERSION

popd

rm -f %{buildroot}%{_libdir}/%{name}/plugins/com.ibm.icu_*

%post platform
%update_icon_cache

%postun platform
%clean_icon_cache

%files ecj
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/dropins
%dir %{_libdir}/%{name}/dropins/jdt
%dir %{_libdir}/%{name}/dropins/jdt/plugins
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.core_*
%{_javadir}/eclipse-ecj*.jar
%{_javadir}/jdtcore*.jar
%{_javadir}/ecj*.jar
%{_bindir}/ecj

%files swt -f %{name}-swt.install
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/libswt-*.so
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/configuration
%dir %{_libdir}/%{name}/configuration/org.eclipse.osgi
%dir %{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles
%{_libdir}/%{name}/plugins/org.eclipse.swt_*
%{_libdir}/%{name}/plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}_*
%{_libdir}/%{name}/swt-gtk*.jar
%{_libdir}/%{name}/swt.jar
%{_jnidir}/swt.jar

%files rcp
%defattr(-,root,root)
%dir %{_libdir}/%{name}/features
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/features
%dir %{_datadir}/%{name}/plugins
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.bundledata*
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.lazy*
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.manager
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.state*
%config %{_libdir}/%{name}/configuration/config.ini
%config %{_libdir}/%{name}/configuration/org.eclipse.equinox.simpleconfigurator/bundles.info
%dir %{_libdir}/%{name}/configuration/org.eclipse.equinox.simpleconfigurator
%{_libdir}/%{name}/notice.html
%{_libdir}/%{name}/epl-v10.html
%{_libdir}/%{name}/links
%ifnarch ppc
%{_libdir}/%{name}/about.html
%endif
%ifarch x86_64
%{_libdir}/%{name}/about_files
%endif
%{_libdir}/%{name}/readme
%{_libdir}/%{name}/startup.jar
%{_libdir}/%{name}/features/org.eclipse.rcp_*
%{_libdir}/%{name}/plugins/org.eclipse.core.commands_*
%{_libdir}/%{name}/plugins/org.eclipse.core.contenttype_*
%{_libdir}/%{name}/plugins/org.eclipse.core.databinding_*
%{_libdir}/%{name}/plugins/org.eclipse.core.databinding.beans_*
%{_libdir}/%{name}/plugins/org.eclipse.core.expressions_*
%{_libdir}/%{name}/plugins/org.eclipse.core.jobs_*
%{_libdir}/%{name}/plugins/org.eclipse.core.runtime_*
%{_libdir}/%{name}/plugins/org.eclipse.core.runtime.compatibility.auth_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.app_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.common_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.launcher_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.launcher.gtk.linux.%{eclipse_arch}_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.preferences_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.help_*
%{_libdir}/%{name}/plugins/org.eclipse.jface_*
%{_libdir}/%{name}/plugins/org.eclipse.jface.databinding_*
%{_libdir}/%{name}/plugins/org.eclipse.osgi_*
%{_libdir}/%{name}/plugins/org.eclipse.rcp_*
%{_libdir}/%{name}/plugins/org.eclipse.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.workbench_*
%{_libdir}/%{name}/plugins/org.eclipse.update.configurator_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.simpleconfigurator_*

%files platform -f %{name}-platform.install
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/%{name}
%config %{_libdir}/%{name}/eclipse.ini
%{_libdir}/%{name}/.eclipseproduct
%{_libdir}/%{name}/configuration/config.ini
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/*/*/apps/*
%{_libdir}/%{name}/eclipse
%dir %{_libdir}/%{name}/dropins
%dir %{_datadir}/%{name}/dropins
%{_libdir}/%{name}/features/org.eclipse.platform_*
%{_libdir}/%{name}/plugins/com.jcraft.jsch_*
%{_libdir}/%{name}/plugins/javax.servlet_*
%{_libdir}/%{name}/plugins/javax.servlet.jsp_*
%{_libdir}/%{name}/plugins/org.apache.ant_*
%{_libdir}/%{name}/plugins/org.apache.commons.el_*
%{_libdir}/%{name}/plugins/org.apache.commons.logging_*
%{_libdir}/%{name}/plugins/org.apache.lucene_*
%{_libdir}/%{name}/plugins/org.apache.lucene.analysis_*
%{_libdir}/%{name}/plugins/org.eclipse.ant.core_*
%{_libdir}/%{name}/plugins/org.eclipse.compare_*
%{_libdir}/%{name}/plugins/org.eclipse.core.boot_*
%{_libdir}/%{name}/plugins/org.eclipse.core.filebuffers_*
%{_libdir}/%{name}/plugins/org.eclipse.core.filesystem_*
%{_libdir}/%{name}/plugins/org.mandriva.ide.platform_*
%{_libdir}/%{name}/features/org.mandriva.ide.feature_*
%{_libdir}/%{name}/plugins/org.eclipse.core.filesystem.linux.%{eclipse_arch}_*
%{_libdir}/%{name}/plugins/org.eclipse.core.net_*
%ifarch %{ix86}
%{_libdir}/%{name}/plugins/org.eclipse.core.net.linux.x86_*
%endif
%{_libdir}/%{name}/plugins/org.eclipse.core.resources_*
%{_libdir}/%{name}/plugins/org.eclipse.core.resources.compatibility_*
%{_libdir}/%{name}/plugins/org.eclipse.core.runtime.compatibility_*
%{_libdir}/%{name}/plugins/org.eclipse.core.runtime.compatibility.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.core.variables_*
%{_libdir}/%{name}/plugins/org.eclipse.debug.core_*
%{_libdir}/%{name}/plugins/org.eclipse.debug.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.http.jetty_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.http.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.http.servlet_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.jsp.jasper_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.jsp.jasper.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.help.appserver_*
%{_libdir}/%{name}/plugins/org.eclipse.help.base_*
%{_libdir}/%{name}/plugins/org.eclipse.help.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.help.webapp_*
%{_libdir}/%{name}/plugins/org.eclipse.jface.text_*
%{_libdir}/%{name}/plugins/org.eclipse.jsch.core_*
%{_libdir}/%{name}/plugins/org.eclipse.jsch.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.ltk.core.refactoring_*
%{_libdir}/%{name}/plugins/org.eclipse.ltk.ui.refactoring_*
%{_libdir}/%{name}/plugins/org.eclipse.osgi.services_*
%{_libdir}/%{name}/plugins/org.eclipse.osgi.util_*
%{_libdir}/%{name}/plugins/org.eclipse.platform_*
%{_libdir}/%{name}/plugins/org.eclipse.platform.doc.user_*
%{_libdir}/%{name}/plugins/org.eclipse.search_*
%{_libdir}/%{name}/plugins/org.eclipse.team.core_*
%{_libdir}/%{name}/plugins/org.eclipse.team.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.text_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.browser_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.cheatsheets_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.console_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.editors_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.externaltools_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.forms_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.ide_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.ide.application_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.intro_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.intro.universal_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.navigator_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.navigator.resources_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.net_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.presentations.r21_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.views_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.views.properties.tabbed_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.workbench.compatibility_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.workbench.texteditor_*
%{_libdir}/%{name}/plugins/org.eclipse.update.core_*
%{_libdir}/%{name}/plugins/org.eclipse.update.core.linux_*
%{_libdir}/%{name}/plugins/org.eclipse.update.scheduler_*
%{_libdir}/%{name}/plugins/org.eclipse.update.ui_*
%{_libdir}/%{name}/plugins/org.mortbay.jetty_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.initializer_*
%{_libdir}/%{name}/plugins/org.eclipse.team.cvs.core_*
%{_libdir}/%{name}/plugins/org.eclipse.cvs_*
%{_libdir}/%{name}/plugins/org.eclipse.team.cvs.ssh2_*
%{_libdir}/%{name}/plugins/org.eclipse.team.cvs.ssh_*
%{_libdir}/%{name}/plugins/org.eclipse.team.cvs.ui_*
%{_libdir}/%{name}/features/org.eclipse.cvs_*
%{_libdir}/%{name}/features/org.eclipse.help_*
%{_libdir}/%{name}/plugins/org.apache.jasper_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.frameworkadmin_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.frameworkadmin.equinox_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.simpleconfigurator.manipulator_*
%{_libdir}/%{name}/features/org.eclipse.equinox.p2.user.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.director_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.core_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.engine_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.jarprocessor_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.metadata_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.metadata.repository_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.artifact.repository_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.exemplarysetup_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.touchpoint.eclipse_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.touchpoint.natives_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.console_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ui.sdk_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.updatechecker_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.garbagecollector_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.directorywatcher_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.reconciler.dropins_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.metadata.generator_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.updatesite_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.security_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.security.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.extensionlocation_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.director.app_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.provider.filetransfer_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.provider.filetransfer.ssl_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.ssl_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.filetransfer_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.identity_*
%{_libdir}/%{name}/plugins/org.sat4j.core_*
%{_libdir}/%{name}/plugins/org.sat4j.pb_*
# Put this in -platform since we're putting the p2 stuff here
%{_libdir}/%{name}/artifacts.xml
# FIXME: should we ship content.xml for the platform?
#%{_libdir}/%{name}/metadata
%{_libdir}/%{name}/p2

%files jdt
%defattr(-,root,root)
%{_bindir}/efj
%{_libdir}/%{name}/dropins/jdt/content.xml
%{_libdir}/%{name}/dropins/jdt/features
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.ant.ui_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.apt.core_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.apt.ui_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.apt.pluggable.core_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.compiler.apt_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.compiler.tool_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.core_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.core.manipulation_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.debug.ui_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.debug_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.junit_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.junit.runtime_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.junit4.runtime_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.launching_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.ui_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.junit_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.junit4_*
%{_libdir}/%{name}/dropins/jdt/plugins/org.eclipse.jdt.doc.user_*

%files pde
%defattr(-,root,root)
%{_libdir}/%{name}/buildscripts
%{_libdir}/%{name}/dropins/sdk
# FIXME:  where should this go?
%{_libdir}/%{name}/configuration/org.eclipse.equinox.source



%changelog
* Sun Feb 20 2011 Oden Eriksson <oeriksson@mandriva.com> 1:3.4.2-0.2.5mdv2011.0
+ Revision: 638871
- sync with MDVSA-2011:032

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1:3.4.2-0.2.4mdv2011.0
+ Revision: 605331
- fix build
- rebuild

* Wed Mar 10 2010 Frederic Crozat <fcrozat@mandriva.com> 1:3.4.2-0.2.3mdv2010.1
+ Revision: 517440
- Force rebuild to try to get eclipse-pde back on repository

* Mon Feb 01 2010 Frederic Crozat <fcrozat@mandriva.com> 1:3.4.2-0.2.2mdv2010.1
+ Revision: 499205
- force rebuild

  + Michael Scherer <misc@mandriva.org>
    - update eclipse-ecj-gcj tarball from cvs, as this fix #44372
      kudos to Andrey Bondrov for the fix

* Sat May 23 2009 Jerome Martin <jmartin@mandriva.org> 1:3.4.2-0.2.0mdv2010.0
+ Revision: 379022
- Fixed link pb (bug #51148)

* Mon Mar 02 2009 Jérôme Soyer <saispo@mandriva.org> 1:3.4.2-0.2.0mdv2009.1
+ Revision: 347361
- Fix icu4j files

* Mon Mar 02 2009 Jérôme Soyer <saispo@mandriva.org> 1:3.4.2-0.1.0mdv2009.1
+ Revision: 347114
- Fix icu4j dir
- New upstream release

* Mon Jan 12 2009 Jérôme Soyer <saispo@mandriva.org> 1:3.4.1-0.14.0mdv2009.1
+ Revision: 328669
- Fix splashscreen

* Mon Jan 12 2009 Jérôme Soyer <saispo@mandriva.org> 1:3.4.1-0.13.0mdv2009.1
+ Revision: 328560
- Fix symlink
- fix build
- Fix patch42
- Fix Source0
- Missing sync patches...
- Include some patch for fixing problems

* Tue Jan 06 2009 Jérôme Soyer <saispo@mandriva.org> 1:3.4.1-0.12.2mdv2009.1
+ Revision: 325506
- Fix another shell scripts
- Fix shell scripts

* Mon Jan 05 2009 Jérôme Soyer <saispo@mandriva.org> 1:3.4.1-0.12.1mdv2009.1
+ Revision: 325138
- Mandriva Custom

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 1:3.4.1-0.12.0mdv2009.1
+ Revision: 324275
- New upstream release
- New upstream release

* Fri Sep 26 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1:3.4.0-0.22.3mdv2009.0
+ Revision: 288591
- BR tomcat5-jsp-2.0-api

* Sat Sep 20 2008 Anssi Hannula <anssi@mandriva.org> 1:3.4.0-0.22.2mdv2009.0
+ Revision: 286261
- provide swt.jar in _jnidir instead of _libdir/java (fixes swt on x86_64)

* Thu Aug 28 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1:3.4.0-0.22.1mdv2009.0
+ Revision: 276803
- add test framework

* Tue Aug 12 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1:3.4.0-0.19.2mdv2009.0
+ Revision: 271182
- fix pdebuild script
- try to symlink swt.jar in /usr/lib/java

* Tue Aug 12 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1:3.4.0-0.19.1mdv2009.0
+ Revision: 271058
- make jdt a dropin not an extension
- create jnidir
- don't link swt.jar in _libdir/java only in _jnidir
- symlink swt.jar in _jnidir

* Fri Aug 08 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1:3.4.0-0.18.1mdv2009.0
+ Revision: 267818
- own dropins/jdt

* Fri Aug 08 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1:3.4.0-0.17.1mdv2009.0
+ Revision: 267805
- really use uname -m
- change uname -p to uname -m for correct arch detection
- add %%{_datadir}/eclipse/droping (sync with fc)
- BR zip
- fix groups
- new version 3.4

* Sun Jun 29 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1:3.3.2-0.9.4mdv2009.0
+ Revision: 230074
- build everything with target 1.6 for the apt things

* Mon Jun 23 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1:3.3.2-0.9.3mdv2009.0
+ Revision: 228281
- rebuilt due to PayloadIsLzma problems

* Sun Jun 22 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1:3.3.2-0.9.2mdv2009.0
+ Revision: 227868
- add missing tomcat5-jasper-eclipse require, disable gcj_compile

* Sat Apr 19 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1:3.3.2-0.9.1mdv2009.0
+ Revision: 195767
- new version

* Tue Feb 26 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1:3.3.1.1-0.14.7mdv2008.1
+ Revision: 175187
- fix internal web browser loading

* Fri Jan 18 2008 David Walluck <walluck@mandriva.org> 1:3.3.1.1-0.14.6mdv2008.1
+ Revision: 154534
- gcj_support does not imply a Requires on java-1.5.0-gcj-javadoc

* Thu Jan 17 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1:3.3.1.1-0.14.5mdv2008.1
+ Revision: 154060
- do not remove already removed jar
- bump release
- fix conflict with tomcat5-jasper-eclipse

* Wed Jan 16 2008 David Walluck <walluck@mandriva.org> 1:3.3.1.1-0.14.4mdv2008.1
+ Revision: 153591
- rebuild

  + Anssi Hannula <anssi@mandriva.org>
    - move jdt.core component from eclipse-ecj to eclipse-jdt and drop
      eclipse-ecj in favor of a new standalone ecj package

  + Alexander Kurtakov <akurtakov@mandriva.org>
    - fix build with tomcat 5.5.25

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 26 2007 David Walluck <walluck@mandriva.org> 1:3.3.1.1-0.14.2mdv2008.1
+ Revision: 137817
- use %%{_jvmdir}/java-gcj/bin/java explicitly for %%{_bindir}/ecj and %%{_bindir}/efj

* Thu Dec 20 2007 David Walluck <walluck@mandriva.org> 1:3.3.1.1-0.14.1mdv2008.1
+ Revision: 135367
- force inclusion of jre/lib/amd64 for icedtea x86-64 workaround
- sync with fedora 14

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Anssi Hannula <anssi@mandriva.org>
    - buildrequire java-rpmbuild, i.e. build with icedtea on x86(_64)

* Mon Nov 26 2007 David Walluck <walluck@mandriva.org> 1:3.3.1.1-0.10.2mdv2008.1
+ Revision: 112008
- bump release
- fix file conflict with icu4j-eclipse
- export LD_LIBRARY_PATH for firefox

* Sun Nov 25 2007 David Walluck <walluck@mandriva.org> 1:3.3.1.1-0.10.1mdv2008.1
+ Revision: 111840
- fix inclusion of %%{_libdir}/gcj/org.eclipse.ui.ide
- fix file list
- BuildRequires: zip
- 3.3.1.1-10

* Sun Nov 18 2007 David Walluck <walluck@mandriva.org> 1:3.3.0-0.30.1mdv2008.1
+ Revision: 109784
- add maxpermsize patch from Fedora
- patch for jsch

* Sun Oct 21 2007 David Walluck <walluck@mandriva.org> 1:3.3.0-0.27.3mdv2008.1
+ Revision: 101059
- do not depend on a specific firefox version

* Sat Oct 20 2007 David Walluck <walluck@mandriva.org> 1:3.3.0-0.27.2mdv2008.1
+ Revision: 100589
- rebuild for new firefox

* Mon Oct 15 2007 David Walluck <walluck@mandriva.org> 1:3.3.0-0.27.1mdv2008.1
+ Revision: 98413
- add versioned and unversioned swt-gtk and swt symlinks
- remove Encoding=UTF-8 from eclipse.desktop
- add org.fedoraproject.ide.feature-1.0.0.zip
- sync with fedora for fedora feature bugfixes
- add missing patch
- add 17vmgenerate16bytecode patch (from Fedora)
- fix java5.home sed line
- fix the eclipse.product in %%install, not post (bug #34399)

* Sat Sep 29 2007 David Walluck <walluck@mandriva.org> 1:3.3.0-0.20.8mdv2008.0
+ Revision: 93915
- set CONFIGURATION_DIR
- really use old launch script

* Thu Sep 27 2007 David Walluck <walluck@mandriva.org> 1:3.3.0-0.20.7mdv2008.0
+ Revision: 93222
- set better values for VM_ARGS
- reintroduce eclipse.conf and old launch script
- remove requires on firefox-devel
- explicitly set MOZILLA_FIVE_HOME to fix loading of firefox
- version Provides and fix Obsoletes versions
- fix the eclipse.product if necessary

* Sat Sep 22 2007 David Walluck <walluck@mandriva.org> 1:3.3.0-0.20.3mdv2008.0
+ Revision: 92120
- don't install or set product to rg.fedoraproject.ide.platform

* Fri Sep 21 2007 David Walluck <walluck@mandriva.org> 1:3.3.0-0.20.2mdv2008.0
+ Revision: 91708
- bump release
- Don't force java >= 1.6.0 requirement
- sync with fc to remove subclipse, changelog, rpm-editor, and mylyn requirements

* Tue Sep 18 2007 David Walluck <walluck@mandriva.org> 1:3.3.0-0.19.3mdv2008.0
+ Revision: 89916
- rebuild
- remove some eclipse Requires (especially eclipse-rpm-editor to allow building)

  + Anssi Hannula <anssi@mandriva.org>
    - require java-gcj for ecj

* Mon Sep 17 2007 Olivier Blin <oblin@mandriva.com> 1:3.3.0-0.18.4mdv2008.0
+ Revision: 89119
- rebuild because of package loss

* Sun Sep 16 2007 Anssi Hannula <anssi@mandriva.org> 1:3.3.0-0.18.3mdv2008.0
+ Revision: 88734
- use system junit
- fix icon, encoding, categories of desktop entry
- rebuild to filter out autorequires of GCJ AOT objects
- remove unnecessary Requires(post) on java-gcj-compat

  + David Walluck <walluck@mandriva.org>
    - bump release
    - we call jetty5 jetty5, whereas fc calls it jetty
    - enable gcj_support for all archs
    - install fc's eclipse script
    - sync with 18fc

* Fri Aug 31 2007 David Walluck <walluck@mandriva.org> 1:3.3.0-0.9.1mdv2008.0
+ Revision: 77167
- sync with 9fc
- change default vm args

* Tue Aug 21 2007 David Walluck <walluck@mandriva.org> 1:3.3.0-0.8.1mdv2008.0
+ Revision: 68690
- remove dup junit4 removal
- sync with 8fc

* Wed Aug 08 2007 David Walluck <walluck@mandriva.org> 1:3.3.0-0.5.4mdv2008.0
+ Revision: 60576
- own %%{_libdir}/%%{name}/features

* Wed Aug 08 2007 David Walluck <walluck@mandriva.org> 1:3.3.0-0.5.3mdv2008.0
+ Revision: 60082
- Requires: icu4j-eclipse

* Tue Aug 07 2007 David Walluck <walluck@mandriva.org> 1:3.3.0-0.5.2mdv2008.0
+ Revision: 59992
- remove some whitespace

* Tue Aug 07 2007 David Walluck <walluck@mandriva.org> 1:3.3.0-0.5.1mdv2008.0
+ Revision: 59646
- don't fork the Jasper compiler
- fix file list
- org.eclipse.ui.ide.application_* is not being built for some reason
- fix sed for efj
- remove ant-bsf, ant-commons-net, and ant-jmf before linking
- whitespace fix
- sync eclipse-ecj-gcj.patch with fc
- modify efj.sh.in with @gccsuffix@ as done in ecj.sh.in
- fix ant symlinks
- set javaHome=%%{java_home} in library/gtk/build.sh
- explicitly require java-1.5.0-gcj-javadoc for build
- link to full jasper5 jar
- sync with latest fedora
- link in jars that now have osgi manifests
- better comments on fedora bugs
- initial work on eclipse 3.3

  + Anssi Hannula <anssi@mandriva.org>
    - replace direct call to ant with %%ant

* Sun Jul 01 2007 Anssi Hannula <anssi@mandriva.org> 1:3.2.2-15.2mdv2008.0
+ Revision: 46801
- use %%gcj and %%gcj_dbtool
- build with system gcc and g++

* Sat Jun 30 2007 Anssi Hannula <anssi@mandriva.org> 1:3.2.2-15.1mdv2008.0
+ Revision: 46136
- fix filelist
- adapt for new tomcat

  + David Walluck <walluck@mandriva.org>
    - put back original junit support
    - (Build)Requires: junit4
    - sync with latest FC release for Java 1.5/1.7 support

* Thu Jun 28 2007 Anssi Hannula <anssi@mandriva.org> 1:3.2.2-8.3mdv2008.0
+ Revision: 45506
- build with gcc4.3

  + David Walluck <walluck@mandriva.org>
    - set correct GCC version (dynamically) in %%{_bindir}/ecj

* Sun Jun 24 2007 Anssi Hannula <anssi@mandriva.org> 1:3.2.2-8.2mdv2008.0
+ Revision: 43605
- fix firefox defines for submitting

  + David Walluck <walluck@mandriva.org>
    - rebuild for new firefox

* Tue May 01 2007 David Walluck <walluck@mandriva.org> 1:3.2.2-8.1mdv2008.0
+ Revision: 19859
- sync with latest fc spec

* Sat Apr 28 2007 David Walluck <walluck@mandriva.org> 1:3.2.2-3.5mdv2008.0
+ Revision: 18914
- sync
- add ecj.jar symlink for JPackage compatibility


* Fri Mar 23 2007 Frederic Crozat <fcrozat@mandriva.com> 1:3.2.2-3.4mdv2007.1
+ Revision: 148400
- Rebuild with latest firefox

  + David Walluck <walluck@mandriva.org>
    - minor fixes

* Fri Mar 16 2007 David Walluck <walluck@mandriva.org> 1:3.2.2-3.2mdv2007.1
+ Revision: 145311
- try to fix conflict with JPackage ecj package

* Fri Mar 16 2007 David Walluck <walluck@mandriva.org> 1:3.2.2-3.1mdv2007.1
+ Revision: 144705
- fix disable-junit4-apt patch
- sync with 3.2.2-3.fc7

  + Per Øyvind Karlsen <pkarlsen@mandriva.com>
    - fix typo in postun for eclipse-sdk

* Tue Mar 13 2007 David Walluck <walluck@mandriva.org> 1:3.2.2-1.9mdv2007.1
+ Revision: 143251
- fix ecj provides

* Mon Mar 12 2007 David Walluck <walluck@mandriva.org> 1:3.2.2-1.8mdv2007.1
+ Revision: 141954
- fix JAVA_HOME setting in Makefile
- allow jsch jar

* Mon Mar 12 2007 David Walluck <walluck@mandriva.org> 1:3.2.2-1.5mdv2007.1
+ Revision: 141543
- build jsch

  + Anssi Hannula <anssi@mandriva.org>
    - fix embedded mozilla browser
    - require only libmozilla-firefox in swt and platform packages
    - replace filename require with package name in eclipse-sdk
    - add swt shared object symlinks back to libdir
    - move swt jar symlinks to jnidir

* Sun Mar 11 2007 David Walluck <walluck@mandriva.org> 1:3.2.2-1.4mdv2007.1
+ Revision: 141375
- require mozilla-firefox not firefox

* Sun Mar 11 2007 David Walluck <walluck@mandriva.org> 1:3.2.2-1.3mdv2007.1
+ Revision: 141371
- replace tabs with spaces
- re-enable osgi for now
- be sure to create libswt3-gtk2.install
- disable junit4-apt on x86
- 3.2.2
- bump release
- fix build
- bump release
- sync better with 37fc
- add ant manifest, xpcom, and native presentation patches (from Debian)
- sync with 37fc

  + Anssi Hannula <anssi@mandriva.org>
    - fix build by dropping patch200 (ant-manifest, from debian)
    - use ant option fork="yes" to fix 64bit code generation
    - drop patch201 (modified generated code)

* Thu Feb 15 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1:3.2.1-4.3mdv2007.1
+ Revision: 121435
- use %%{sunsparc} macro

  + David Walluck <walluck@mandriva.org>
    - update (Build)Requires and symlinks for ant 1.7.0
    - fix build with firefox
    - bump release
    - fix firefox patch
    - don't try to remove icu4j twice
    - don't require icu4j to build
    - build icu4j internally for now
    - fix icu4j version
    - update patches
    - 3.2.1
    - Import eclipse

* Tue Sep 19 2006 Frederic Crozat <fcrozat@mandriva.com> 1:3.2.0-12.3mdv2007.0
- Fix firefox dependency

* Sun Sep 03 2006 David Walluck <walluck@mandriva.org> 0:3.2.0-12.2mdv2007.0
- fix jsch jar creation

* Sun Aug 27 2006 David Walluck <walluck@mandriva.org> 0:3.2.0-12mdv2007.0
- (Build)Requires: ant-manifest-only
- sync with 12fc

* Sat Aug 05 2006 David Walluck <walluck@mandriva.org> 0:3.2.0-10mdv2007.0
- use sed for tomcat version
- add xpcom patch

* Sun Jul 23 2006 David Walluck <walluck@mandriva.org> 0:3.2.0-5mdv2007.0
- add ecj-gcj patch
- use a different fix for swt symlink

* Fri Jul 21 2006 David Walluck <walluck@mandriva.org> 0:3.2.0-3mdv2007.0
- fix CLASSPATH
- fix build

* Mon Jul 10 2006 David Walluck <walluck@mandriva.org> 0:3.2.0-2mdv2007.0
- fix run on x86-64
- fix swt symlink
- use %%update_icon_cache and %%clean_icon_cache

* Sun Jul 09 2006 David Walluck <walluck@mandriva.org> 0:3.2.0-1mdv2007.0
- 3.2.0

* Tue Jun 06 2006 David Walluck <walluck@mandriva.org> 0:3.1.2-7mdv2007.0
- make symlink for jdtcore.jar (bug #22574)
- replace %%{_datadir}/java with %%{_javadir}

* Tue Jun 06 2006 David Walluck <walluck@mandriva.org> 0:3.1.2-6mdv2007.0
- fix ecj script

* Wed Apr 26 2006 David Walluck <walluck@mandriva.org> 0:3.1.2-5mdv2007.0
- rebuild for libgcj.so.7
- remove explicit libgcj dependency

* Thu Apr 13 2006 David Walluck <walluck@mandriva.org> 0:3.1.2-4mdk
- modify rebuild-sdk-features to exit silently if no configuration
  exists

* Wed Apr 12 2006 David Walluck <walluck@mandriva.org> 0:3.1.2-3mdk
- sync with 1jpp_13fc

* Mon Apr 10 2006 David Walluck <walluck@mandriva.org> 0:3.1.2-2mdk
- fix tomcat version and require it explicitly (bug #21681)
- disable install into %%{_datadir}/%%{name}/configuration
  (bug #21682)
- append -mdk to CONFIGURATION_DIR in eclipse.conf and don't set
  USER_DIR in eclipse.conf, but no patch for now (bug #21694)
- make eclipse-platform require ant-jai and ant-jmf (bug #21694) 
- rebuild to fix mozilla-firefox dependencies (bug #21858)
- fix setting of VM_OPTS in /usr/bin/eclipse and set
  VM_OPTS="-Dgnu.gcj.runtime.VMClassLoader.library_control=never"
  (bug #21883)
- use eclipse png icons included in platform plugin

* Tue Feb 07 2006 David Walluck <walluck@mandriva.org> 0:3.1.2-1mdk
- 3.1.2
- add Debian menu
- use gcjdb macros

* Thu Jan 12 2006 David Walluck <walluck@mandriva.org> 0:3.1.1-8mdk
- fix file conflict between eclipse-ecj and eclipse-jdt

* Thu Jan 05 2006 David Walluck <walluck@mandriva.org> 0:3.1.1-7mdk
- sync with 3.1.1-1jpp_15fc
- link against mozilla-firefox
- remove extra description

* Fri Nov 11 2005 David Walluck <walluck@mandriva.org> 0:3.1.1-6mdk
- sync with 3.1.1-1jpp_6fc (enable cairo)

* Sun Nov 06 2005 David Walluck <walluck@mandriva.org> 0:3.1.1-5mdk
- patch launchersrc

* Mon Oct 31 2005 David Walluck <walluck@mandriva.org> 0:3.1.1-4mdk
- replace firefox by mozilla until at least mozilla works
- fix loading of mozilla
- add patches from Debian (mozilla l&f and disable motif)

* Tue Oct 25 2005 David Walluck <walluck@mandriva.org> 0:3.1.1-3mdk
- add back changes to eclipse{.conf,.script,-libswt-mozilla.patch}
- require lucene-src

* Fri Oct 14 2005 David Walluck <walluck@mandriva.org> 0:3.1.1-2mdk
- apply patch for eclipse bug #111299
- add BuildRequires for desktop-file-utils

* Thu Oct 13 2005 David Walluck <walluck@mandriva.org> 0:3.1.1-1mdk
- 3.1.1
- fix libswt symlinks

* Sun Sep 18 2005 David Walluck <walluck@mandriva.org> 0:3.1.0-8mdk
- cairo 1.0 doesn't work out of the box

* Wed Sep 14 2005 David Walluck <walluck@mandriva.org> 0:3.1.0-7mdk
- fix build on x86_64
- fix startup script
- fix ant script symlinks

* Mon Sep 12 2005 David Walluck <walluck@mandriva.org> 0:3.1.0-6mdk
- remove /usr/bin/mozilla requirement for eclipse-platform
- don't enable embedded mozilla-firefox browser by default (crashes)
- use eclipse-ecj (ecj-bootstrap) to build until gcj works again

* Fri Sep 09 2005 David Walluck <walluck@mandriva.org> 0:3.1.0-5mdk
- use mozilla-firefox instead of mozilla

* Wed Sep 07 2005 David Walluck <walluck@mandriva.org> 0:3.1.0-4mdk
- provide and obsolete ecj-bootstrap

* Tue Sep 06 2005 David Walluck <walluck@mandriva.org> 0:3.1.0-3mdk
- simplify mozilla-gtkmozembed cflags and libs

* Tue Sep 06 2005 David Walluck <walluck@mandriva.org> 0:3.1.0-2mdk
- update main and platform description with info about native libs
- remove patch32 (enable cairo)

* Sat Sep 03 2005 David Walluck <walluck@mandriva.org> 0:3.1.0-1mdk
- release

* Fri Jul 29 2005 Gary Benson <gbenson@redhat.com> 3.1.0_fc-12
- Allow leading separators in classpaths (e.o#105430).
- Clear away ant-jmf entirely.

* Thu Jul 28 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-11
- Bump release for FC4 update.

* Tue Jul 26 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-10
- Change mozilla BuildRequirement to be equals and not greater-than or equals
  since we need the exact version for our patches.
- Bump mozilla requirements and patches to 1.7.10.
- Bump release due to FC4 update still not being released.
- Add ant-jmf to exclude list.

* Wed Jul 20 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-7
- Remove ant-jmf symlinking and requirement.
- Update to use java-gcj-compat and not java-1.4.2-gcj-compat.

* Wed Jul 13 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-6
- Bump release to build against new gcc.
- Bump gcc requirement to gcc 4.0.1.
- Add back BuildArch until we get bootstrapping sorted out.
- Bump required version of java-gcj-compat to the latest (-40jpp_37rh).
- Remove lots of jiggery-pokery with native compilation and use gbenson's new
  aot-compile.
- Re-work files sections appropriately.
- Change mozilla-nspr-devel -> nspr-devel due to change in mozilla packaging.
- Update patch for mozilla build as per above.
- Add org.eclipse.osgi_3.1.0.jar to exclude.

* Wed Jul 06 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-5
- Revert ecj_bootstrap patch since it won't work.
- Keep mozilla requirement off ppc64.
- Add ant-apache-bsf requirement since we have that in FC5.

* Wed Jul 06 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-4
- Add ecj_bootstrap patch from Gary Benson to bootstrap new architectures.
- Remove ExclusiveArch.

* Wed Jul 06 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-3
- Bump release for FC4 update.

* Tue Jul 05 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-2
- Remove remaining pre-built ant jars (but don't symlink to ant.jar until we
  have ant 1.6.5 - rh#162444).
- Bump requirement on gcc to get fixes for rh#158614 and gcc#21637.
- Add patch to not try to link to external javadocs and include the javadoc
  output in the build output.
- Add build and runtime requirement on ant-javamail (I'm not sure how we missed
  this previously).

* Tue Jul 05 2005 Gary Benson <gbenson@redhat.com> 3.1.0_fc-2
- Disable classpath access rules introduced in e.o#92398 (rh#162177).

* Wed Jun 29 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-1
- Import 3.1.
- Update splash screen.

* Mon Jun 27 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.RC4.1
- Import 3.1 RC4.
- Remove activeHelpSample.jar building patch as it's now fixed upstream.
- Add patch to remove references to cairo since we don't have it in FC4.
- Add about.html and about_files to eclipse-platform.install (x86 & x86_64).
- Add patch to create public compare API (jpound - e.o#98707).
- Add patch from Robin Green to not look for firefox libxpcom.so (rh#161658).
- Symlink lucene jars (rh#159939).

* Sat Jun 25 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.RC3.3
- Add rcp requirement for platform (rh#161267).
- Add un-owned osgi directories to libswt and platform.

* Wed Jun 22 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.RC3.2
- Use SWT bundle ID for SWT %%files list (determine in %%install).

* Tue Jun 21 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.RC3.1
- Import 3.1RC3.
- Use FileInitializer (e.o#90535) - this should eliminate .sos in ~/.eclipse.
- Add eclipse-filenamepatterns.txt ("*.so" currently) for above.
- Symlink JNI libraries.

* Sat Jun 18 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.RC2.2
- Update to new naming scheme for resulting gzipped tarball.
- Add patch to not generate help indices (it seems to hang).

* Fri Jun 17 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.RC2.1
- Import 3.1RC2.
- Add RCP sub-package.  Unsure about its dependencies ATM.

* Wed Jun 15 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M7.9
- Add tomcat5 patch and symlinks.

* Fri May 27 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M7.8
- Fix ant jar removal (gbenson).

* Thu May 26 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M7.7
- Fix ecj symlink in /usr/share/java (rh#158734).

* Mon May 23 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M7.4
- Remove compilation of jdt.ui jar.so on ppc.

* Sun May 22 2005 Ben Konrath <bkonrath@redhat.com> 3.1.0_fc-0.M7.3
- Add ecj-options patch to bootstrap source.
- Make embedded browser widget work (Robin Green).
- Bump required version of java-gcj-compat to the latest (-40jpp_24rh).
- Use -lgcjawt when building with gcj.

* Thu May 19 2005 Ben Konrath <bkonrath@redhat.com> 3.1.0_fc-0.M7.2
- Disable org.eclipse.osgi_3.1.0.jar.so.
- Add ecj-options patch, remove ecj-extdirs patch.

* Thu May 19 2005 Ben Konrath <bkonrath@redhat.com> 3.1.0_fc-0.M7.1
- Update to 3.1M7.
- Add file initializer patch.
- Temporarily remove s390{,x} patches.
- Update GNU formatter ui patch.
- Add ECJ ext dirs patch.

* Wed May 18 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M6.19
- Add Epoch on eclipse-platform.
- Use %%{_bindir} in post and postun scripts.

* Wed May 18 2005 Ben Konrath <bkonrath@redhat.com> 3.1.0_fc-0.M6.18
- Add Epoch to jsch requires.

* Tue May 17 2005 Ben Konrath <bkonrath@redhat.com> 3.1.0_fc-0.M6.17
- Update libswt-mozilla patches and require mozilla 1.7.8.

* Sat May 14 2005 Andrew Overholt <overholt@redhat.com>
- Use %%{ix86} macro in ExclusiveArch rather than i386 (jorton).

* Thu May 12 2005 Ben Konrath <bkonrath@redhat.com>
- Add jsch >= 0.1.18-1jpp.
- Remove Fedora specific part of junit version.
- Temporarily disable org.eclipse.ui.forms_3.1.0.jar.so (rh#146463).

* Tue May 10 2005 Ben Konrath <bkonrath@redhat.com> 3.1.0_fc-0.M6.16
- Add Requires junit >= 3.8.1-3jpp_4fc to JDT.
- Add -g to gcj calls.

* Fri May 06 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M6.15
- Rebuild with new gjdoc (rh#152049).

* Thu May 05 2005 Ben Konrath <bkonrath@redhat.com>
- Re-enable jdt.ui/jdt.jar.so and require gcj 4.0.0-2 (rh#151296).

* Tue May 03 2005 Ben Konrath <bkonrath@redhat.com> 3.1.0_fc-0.M6.14
- Replace temporary patch to debug.ui with upstream patch to swt (rh#155853).

* Sun May 01 2005 Ben Konrath <bkonrath@redhat.com> 3.1.0_fc-0.M6.13
- Add patch to temporarily stop an NPE in debug.ui (rh#155853).

* Fri Apr 29 2005 Phil Muldoon <pmuldoon@redhat.com>
- Allow multiple optional arguments in eclipse-copy-platform.sh

* Thu Apr 28 2005 Andrew Overholt <overholt@redhat.com>
- Include epoch in mozilla BuildRequires.
- Remove last remaining gij-specific option from eclipse.script.

* Thu Apr 28 2005 Jeremy Katz <katzj@redhat.com> 3.1.0_fc-0.M6.12
- silence %%post

* Mon Apr 25 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M6.11
- Re-add osgi.jar.so since gcj fix is in our gcc RPMs.
- Bump gcc requirements accordingly.
- Add gcc-c++ to BuildRequires (for SWT Mozilla).
- Add specific java-1.4.2-gcj-compat nvr requirement (rh#151866).

* Sat Apr 23 2005 Aaron Luchko <aluchko@redhat.com> 3.1.0_fc-0.M6.10
- Import archived projects (e.o#82988)

* Sat Apr 23 2005 Andrew Overholt <overholt@redhat.com>
- Add Requires(post,postun): java-1.4.2-gcj-compat for each sub-package and use
  full path (Joe Orton).
- Make /usr/bin/eclipse executable again (rh#155715).
- Bump jsch version.

* Fri Apr 22 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M6.9
- Use upstream icons (not RHDS ones) (rh#146484).
- Add plugin directories to %%files sections.
- Rework %%files sections a bit.
- Fix SWT symlink (bkonrath).
- Temporarily remove jdt.ui/jdt.jar.so.

* Fri Apr 22 2005 Ben Konrath <bkonrath@redhat.com> 3.1.0_fc-0.M6.8
- Fix updatesite patch.
- Temporarily remove org.eclipse.ui.workbench_3.1.0.jar.so (r.c#151919)

* Tue Apr 19 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M6.7
- Add %%if %%{gcj_support} blocks.
- Add %%{_libdir}/%%{name}/plugins to native %%files section of each sub-rpm.
- Add GNU-style JDT code formatting option (e.o#91770).
- Add patch to install plugins from update site in home dir (e.o#90630).
- Change gcc-java requirements to libgcj as gcj-dbtool is now in the latter.

* Tue Apr 19 2005 Ben Konrath <bkonrath@redhat.com> 3.1.0_fc-0.M6.6
- Bump version number.

* Tue Apr 19 2005 Ben Konrath <bkonrath@redhat.com> 3.1.0_fc-0.M6.5
- Update mozilla patch.

* Sun Apr 17 2005 Ben Konrath <bkonrath@redhat.com> 3.1.0_fc-0.M6.4
- Update to 3.1M6.
- Change bootstrap procedure to match the upstream method.
- Remove patches that were fixed upstream. 
- Add efj wrapper script.

* Thu Apr 14 2005 Ben Konrath <bkonrath@redhat.com> 3.1.0_fc-0.M5.20
- Fix the bootstrap patch (the ecj jar was missing some files).

* Wed Apr 13 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M5.19
- Add Requires(post,postun): java-1.4.2-gcj-compat for rebuild-gcj-db (Joe
  Orton).
- Add ecj binary.

* Thu Apr 07 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M5.18
- Fix typo in gcj db building loops.
- Add -O1 to x86_64 jar.so compilation.
- Add EFJ (Eclipse Formatter for Java) patches (bkonrath) (e.o#75333).
- Add patch to build swttools.jar (e.o#90364).
- Symlink out to ant-jsch now that we have that.

* Tue Apr 05 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M5.17
- Actually insert .jar-.jar.so combinations into sub-dbs.

* Fri Apr 01 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M5.16
- Fix eclipse.script to not leave a sh process around (Joe Orton)
- Use proper sub-dbs.
- Don't compile jars that are symlinked from elsewhere.
- Add jar-so combinations to .db based on .jar.so existence (not .jar).
- Rename sub-dbs to be eclipse-*.db.
- Use rebuild-gcj-db script.

* Tue Mar 29 2005 Christopher Aillon <caillon@redhat.com>
- rebuilt

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 3.1.0_fc-0.M5.14
- Update the GTK+ theme icon cache on (un)install

* Fri Mar 18 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M5.13
- Re-add compilation of resources.jar.
- Backport bootstrapping patch.
- Add Requires: java-1.4.2-gcj-compat.
- Modified find patch courtesy Ziga Mahkovec (RH#149927#).
- Compile with -O2 on ppc as well.
- Add jsch, jakarta-commons-modeler, and mx4j symlinking.
- Make use of gcj-dbtool -f to create databases in install.
- Use system-wide classmap.db.
- Remove *.jarswithnativelibs from files sections.
- Update mozilla dependency.

* Mon Mar 07 2005 Ben Konrath <bkonrath@redhat.com> 3.1.0_fc-0.M5.12
- Add activeHelpSample.jar patch.
- Change to Fedora M-build splash screen.
- Add find patch courtesy Ziga Mahkovec (RH#149927#)
- Build native stuff with -O2 on i386.

* Mon Mar 07 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M5.11
- Add s390 and s390x patches.
- Don't build for them, though, due to gcc bug and Eclipse building issue.
- Add xorg-x11-devel BuildRequires.

* Fri Mar 04 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M5.10
- Add proper mozilla version.
- Don't build eclipseAdaptor.jar.so in order to work around plugin building
  problems.

* Thu Mar 03 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M5.9
- Add patch to build libswt-mozilla.
- Build libswt-awt.
- Add 64-bit swt lib list.

* Tue Mar 01 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M5.8
- Add ppc.
- Add patch to copy over icon for unsupported (upstream) platforms but don't
  include the source for the launcher.
- gcc4 -> gcc changes.
- Add swt-cairo to 64-bit platforms' %%files.

* Fri Feb 25 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M5.7
- Add tar args patch (e.o #86571).
- New build bootstrapping patches.

* Fri Feb 25 2005 Andrew Overholt <overholt@redhat.com> 3.1.0_fc-0.M5.6
- Re-work how we do the gcj-dbtool magic.
- Don't remove ant-netrexx (need to find an RPM if we can).

* Sun Feb 20 2005 Andrew Overholt <overholt@redhat.com> 1:3.1_fc-0.M5.5
- Build for just i386 and x86_64 for now due to upstream gcc bugs.

* Sun Feb 20 2005 Andrew Overholt <overholt@redhat.com> 1:3.1_fc-0.M5.1
- New 3.1M5a build using upstream build method.
- Re-organize sub-packages (ecj, platform, platform-devel, jdt, jdt-devel, pde,
  pde-devel, fold gtk2 package into platform).
- Move jface and org.eclipse.text into libswt3-gtk2.
- Bring in JPackage symlinks for packages we have in Fedora (David Walluck) and
  put in %%prep.
- Work around x86_64 filename differences.
- Remove xerces, xalan, and xml-commons-apis requirement (and LD_PRELOAD from
  script).
- Bootstrap build.

