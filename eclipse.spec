# TODO:
# - get someone to update the splash screen properly
# - update icu4j and jasper to use %%{_libdir}/eclipse and not %%{_datadir}/eclipse after we build 3.4
# - update ecj-rpmdebuginfo patch
# - look at startup script and launcher patches
# - get Ganymede update site pre-configured
# - investigate bi-arch requirements
# - see why about.html isn't being copied on ppc
Epoch:  1

%define eclipse_major   3
%define eclipse_minor   4
%define eclipse_majmin  %{eclipse_major}.%{eclipse_minor}
%define eclipse_micro   0
%define swtver          3.4.0.v3448f

# Prevent brp-java-repack-jars from being run.
%define __jar_repack 0

# All arches line up between Eclipse and Linux kernel names except i386 -> x86
%ifarch %{ix86}
%define eclipse_arch    x86
%else
%define eclipse_arch   %{_arch}
%endif

Summary:        An open, extensible IDE
Name:           eclipse
Version:        %{eclipse_majmin}.%{eclipse_micro}
Release:        %mkrel 0.15.0.2
License:        EPL
Group:          Development/Java
URL:            http://www.eclipse.org/
Source0:        http://download.eclipse.org/eclipse/downloads/drops/R-3.4-200806172000/eclipse-sourceBuild-srcIncluded-3.4.zip
Source2:        %{name}.desktop
#Source3:        eclipse.in
# cvs -d :pserver:anonymous@sources.redhat.com:/cvs/eclipse export \
#   -r fedoraeclipse-3_4_0-1 branding/org.fedoraproject.ide.platform
# cd branding
# zip -r org.fedoraproject.ide.platform-3.4.0-1.zip \
#   org.fedoraproject.ide.platform
Source4:        org.fedoraproject.ide.platform-%{version}-1.zip
# cvs -d :pserver:anonymous@sources.redhat.com:/cvs/eclipse export \
#   -r fedoraeclipsefeature-1_0_0 branding/org.fedoraproject.ide-feature
# cd branding
# zip -r org.fedoraproject.ide.feature-1.0.0.zip \
#   org.fedoraproject.ide-feature
Source5:        org.fedoraproject.ide.feature-1.0.0.zip
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
# export -r eclipse_r34 eclipse-gcj
# tar cjf eclipse-ecj-gcj.tar.bz2 eclipse-gcj
Source29:       %{name}-ecj-gcj.tar.bz2

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
#Patch14:        %{name}-ecj-rpmdebuginfo.patch
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
Patch33:	%{name}-pdeapicasting.patch
Patch34:	%{name}-pdeapicasting-ui.patch

# Make ECF bundles have the same qualifier as they do upstream
Patch35:	%{name}-ecf-qualifier.patch

# Don't pack the icu4j source bundle.  Can go away when we re-build
# icu4j against a 3.4 SDK.
Patch36:	%{name}-dontpackicu4jsource.patch

# Our dependent JARs have different signatures than the ones included
# upstream so remove the signatures in the manifests
Patch37:	%{name}-nojarsignatures.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  ant
BuildRequires:  jpackage-utils >= 0:1.5, make, gcc
BuildRequires:  gnome-vfs2-devel
BuildRequires:  gtk2-devel
BuildRequires:  glib2-devel
BuildRequires:  libgnome2-devel
BuildRequires:  libgnomeui2-devel
BuildRequires:  gcc-c++
BuildRequires:  xulrunner-devel >= 1.9
BuildRequires:  nspr-devel
BuildRequires:  libxtst-devel
BuildRequires:  mesagl-devel
BuildRequires:  mesaglu-devel
BuildRequires:  cairo >= 1.0
BuildRequires:  unzip
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
Requires:           icu4j-eclipse >= 3.6.1-1jpp.4
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
Requires: jetty5
Requires: jsch >= 0.1.31
Requires: lucene >= 1.9.1
Requires: lucene-contrib >= 1.9.1
Requires: regexp
Requires: sat4j
Provides: eclipse-cvs-client = 1:%{version}-%{release}
Obsoletes: eclipse-cvs-client < 1:3.3.2-20

%description    platform
The Fedora Eclipse Platform is the base of all IDE plugins.  This does not include the
Java Development Tools or the Plugin Development Environment.

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

# Use ECJ for GCJ's bytecode compiler
tar jxf %{SOURCE29}
mv eclipse-gcj/org/eclipse/jdt/internal/compiler/batch/GCCMain.java \
  plugins/org.eclipse.jdt.core/batch/org/eclipse/jdt/internal/compiler/batch/
mv eclipse-gcj/gcc.properties \
  plugins/org.eclipse.jdt.core/batch/org/eclipse/jdt/internal/compiler/batch/
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

#%patch14 -p0

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

pushd plugins/org.eclipse.pde.api.tools
%patch33
popd
pushd plugins/org.eclipse.pde.api.tools.ui
%patch34
popd

%patch36
%patch37

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
ln -s %{_javadir}/org.sat4j.core_* plugins/
ln -s %{_javadir}/org.sat4j.pb_* plugins/

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
#ln -s %{_javadir}/ant/ant-apache-bsf.jar $ANTDIR/ant-apache-bsf.jar
ln -s %{_javadir}/ant/ant-apache-log4j.jar $ANTDIR/ant-apache-log4j.jar
ln -s %{_javadir}/ant/ant-apache-oro.jar $ANTDIR/ant-apache-oro.jar
ln -s %{_javadir}/ant/ant-apache-regexp.jar $ANTDIR/ant-apache-regexp.jar
ln -s %{_javadir}/ant/ant-apache-resolver.jar $ANTDIR/ant-apache-resolver.jar
ln -s %{_javadir}/ant/ant-commons-logging.jar $ANTDIR/ant-commons-logging.jar
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=180642
# the symlinks that are commented-out are not currently shipped on Fedora
#ln -s %{_javadir}/ant/ant-commons-net.jar $ANTDIR/ant-commons-net.jar
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
ln -s %{_datadir}/eclipse/plugins/com.ibm.icu_*.jar plugins/com.ibm.icu_$ICUVERSION

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

%install
rm -rf $RPM_BUILD_ROOT

# Get swt version
SWT_MAJ_VER=$(grep maj_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_MIN_VER=$(grep min_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_VERSION=$SWT_MAJ_VER$SWT_MIN_VER

# Some directories we need
sdkDir=$RPM_BUILD_ROOT%{_libdir}/%{name}
install -d -m 755 $sdkDir
install -d -m 755 $sdkDir/plugins
install -d -m 755 $sdkDir/features
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/java
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
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

LAUNCHERVERSION=$(ls $sdkDir/plugins | grep equinox.launcher_ | sed 's/org.eclipse.equinox.launcher_//')

# Install the file initializer app
cp -p equinox-incubator/org.eclipse.equinox.initializer/org.eclipse.equinox.initializer_*.jar \
  $sdkDir/plugins

# Install the Fedora Eclipse product plugin
unzip -qq -d $sdkDir/plugins %{SOURCE4}
# Install the Fedora Eclipse product feature
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
java \
-cp $installDir/plugins/org.eclipse.equinox.launcher_$LAUNCHERVERSION \
org.eclipse.core.launcher.Main \
-application \
org.eclipse.equinox.p2.metadata.generator.EclipseGenerator \
-metadataRepository file:$metadataDir \
-artifactRepository file:$metadataDir \
-source $installDir \
-root "Fedora Eclipse Platform" \
-rootVersion %{version} \
-flavor tooling \
-publishArtifacts \
-append \
-artifactRepositoryName "Fedora Eclipse" \
-metadataRepositoryName "Fedora Eclipse"

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
java \
-cp $installDir/plugins/org.eclipse.equinox.launcher_$LAUNCHERVERSION \
org.eclipse.core.launcher.Main \
-application \
org.eclipse.equinox.p2.metadata.generator.EclipseGenerator \
-metadataRepository file:$jdtMetadata \
-artifactRepository file:$jdtMetadata \
-source $jdtDir \
-root "Fedora Eclipse JDT" \
-rootVersion %{version} \
-flavor tooling \
-append \
-artifactRepositoryName "Fedora Eclipse" \
-metadataRepositoryName "Fedora Eclipse"

# SDK
sdkMetadata=$sdkDir/metadata-SDK

# Generate metadata for SDK
java \
-cp $installDir/plugins/org.eclipse.equinox.launcher_$LAUNCHERVERSION \
org.eclipse.core.launcher.Main \
-application \
org.eclipse.equinox.p2.metadata.generator.EclipseGenerator \
-metadataRepository file:$sdkMetadata \
-artifactRepository file:$sdkMetadata \
-source $sdkDir \
-root "Fedora Eclipse SDK" \
-rootVersion %{version} \
-flavor tooling \
-publishArtifacts \
-append \
-artifactRepositoryName "Fedora Eclipse" \
-metadataRepositoryName "Fedora Eclipse"

# Director config.ini
mv $installDir/configuration/config.ini{,.bak}
cp -p %{SOURCE22} $installDir/configuration/config.ini

# Debugging?  Add -debug and -consolelog
# Provision with director
java \
-Declipse.p2.data.area=file://$provisionDir/p2 \
-cp $installDir/plugins/org.eclipse.equinox.launcher_$LAUNCHERVERSION \
org.eclipse.core.launcher.Main \
-application \
org.eclipse.equinox.p2.director.app.application \
-flavor tooling \
-installIU "Fedora Eclipse Platform" \
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
dropins=$provisionDir/dropins
mkdir $dropins/jdt $dropins/sdk
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
sed -i "s|file\:$provisionDir/\ -\ bundle\ pool|Fedora Eclipse|g" \
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
java -Dosgi.sharedConfiguration.area=$libdir_path/configuration \
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

# Set eclipse.product to org.fedoraproject.ide.platform 
sed --in-place "s/plugins\/org.eclipse.platform/plugins\/org.fedoraproject.ide.platform/" \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/configuration/config.ini
sed --in-place "s/eclipse.product=org.eclipse.platform.ide/eclipse.product=org.fedoraproject.ide.platform.product/" \
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

# Set up an extension location and a link file for the arch-independent dir
echo "path:%{_datadir}" > \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/links/datadir.link

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
  ln -s $lib `basename $lib`
done
popd

# Install the SWT jar symlinks in libdir
SWTJARVERSION=$(grep v$SWT_VERSION plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}/build.xml | sed "s:.*<.*\"\(.*\)\"/>:\1:")
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
ln -s plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}_$SWTJARVERSION.jar swt-gtk-%{eclipse_majmin}.%{eclipse_micro}.jar
ln -s swt-gtk-%{eclipse_majmin}.%{eclipse_micro}.jar swt-gtk-%{eclipse_majmin}.jar
ln -s swt-gtk-%{eclipse_majmin}.%{eclipse_micro}.jar swt.jar
ln -s ../%{name}/swt-gtk-%{eclipse_majmin}.%{eclipse_micro}.jar ../java/swt.jar
popd

# Install the eclipse-ecj.jar symlink for java-1.4.2-gcj-compat's "javac"
JDTCORESUFFIX=$(ls $RPM_BUILD_ROOT%{_libdir}/%{name}/dropins/jdt/plugins | grep jdt.core_ | sed "s/org.eclipse.jdt.core_//")
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
ln -s %{_libdir}/%{name}/plugins/org.fedoraproject.ide.platform/eclipse48.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
ln -s %{_libdir}/%{name}/plugins/org.fedoraproject.ide.platform/eclipse32.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
ln -s %{_libdir}/%{name}/plugins/org.fedoraproject.ide.platform/eclipse.png \
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
ln -s %{_javadir}/org.sat4j.core_* plugins/
ln -s %{_javadir}/org.sat4j.pb_* plugins/

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
#ln -s %{_javadir}/ant/ant-apache-bsf.jar $ANTDIR/ant-apache-bsf.jar
ln -s %{_javadir}/ant/ant-apache-log4j.jar $ANTDIR/ant-apache-log4j.jar
ln -s %{_javadir}/ant/ant-apache-oro.jar $ANTDIR/ant-apache-oro.jar
ln -s %{_javadir}/ant/ant-apache-regexp.jar $ANTDIR/ant-apache-regexp.jar
ln -s %{_javadir}/ant/ant-apache-resolver.jar $ANTDIR/ant-apache-resolver.jar
ln -s %{_javadir}/ant/ant-commons-logging.jar $ANTDIR/ant-commons-logging.jar
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=180642
# the symlinks that are commented-out are not currently shipped on Fedora
#ln -s %{_javadir}/ant/ant-commons-net.jar $ANTDIR/ant-commons-net.jar
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
ln -s %{_datadir}/eclipse/plugins/com.ibm.icu_*.jar plugins/com.ibm.icu_$ICUVERSION

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

%clean
rm -rf $RPM_BUILD_ROOT

%post platform
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%postun platform
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

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
%{_libdir}/java/swt.jar

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
%{_libdir}/%{name}/plugins/com.ibm.icu_*

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
%{_libdir}/%{name}/plugins/org.fedoraproject.ide.platform_*
%{_libdir}/%{name}/features/org.fedoraproject.ide.feature_*
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

