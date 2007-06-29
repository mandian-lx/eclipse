Epoch:  1

%define gcj_support     1
%define tomcatepoch     0
%define tomcatversion   5.5.17
%define tomcatsharedir  %{_datadir}/tomcat5
%define tomcatlibdir    %{_var}/lib/tomcat5
%define firefox_version %(rpm -q mozilla-firefox --queryformat %{VERSION} 2>/dev/null)
%define firefox_dir     %(firefox-config --defines 2>/dev/null | sed -n -e 's,.*MOZ_DEFAULT_MOZILLA_FIVE_HOME=\\"\\([^\\"]*\\)\\"\\(.*\\),\\1,p')
%define section         free
%define eclipse_major   3
%define eclipse_minor   2
%define eclipse_majmin  %{eclipse_major}.%{eclipse_minor}
%define eclipse_micro   2
%define libname         libswt3

%define gccsuffix	4.3

# All archs line up between Eclipse and Linux kernel names except i386 -> x86
%ifarch %{ix86}
%define eclipse_arch    x86
%else
%define eclipse_arch   %{_arch}
%endif

Summary:        An open, extensible IDE
Name:           eclipse
Version:        %{eclipse_majmin}.%{eclipse_micro}
Release:        %mkrel 15.1
License:        EPL
Group:          Development/Java
URL:            http://www.eclipse.org/
Source0:        http://download.eclipse.org/eclipse/downloads/drops/R-3.2.2-200702121330/eclipse-sourceBuild-srcIncluded-3.2.2.zip
Source1:        %{name}.script
Source2:        %{name}.desktop
Source6:        %{name}.conf
# The icu4j bits will be moved out into their own package for Fedora 7.  See:
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=199504
Source7:        ftp://ftp.software.ibm.com/software/globalization/icu/icu4j/3.4.5/icu4jsrc_3_4_5.jar
Source11:       %{name}-fedora-splash-3.2.2.png
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

# Build liblocalfile and libupdate JNI libs in the main SDK build.xml
Patch0:         %{name}-build.patch
# We need this because icu4j's Eclipse bits are dependent upon Eclipse
# but we don't want the icu4j RPM needing Eclipse to build
Patch1:         %{name}-icu4j-build-files.patch
# These two patches need to go upstream
Patch2:         %{name}-libupdatebuild.patch
Patch3:         %{name}-libupdatebuild2.patch
# Build swttools.jar
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=90364
Patch4:         %{name}-swttools.patch
# This needs to go upstream
Patch11:        %{name}-usebuiltlauncher.patch
# This does two things:
# 1. allows the launcher to be in /usr/bin and
# 2. ensures that the OSGi configuration directory
#    (which contains the JNI .sos) is in %{_libdir}
# We should investigate whether or not this can go upstream
Patch12:        %{name}-launcher-set-install-dir-and-shared-config.patch
# Always generate debug info when building RPMs (Andrew Haley)
# This needs to be investigated for getEnv changes
Patch14:        %{name}-ecj-rpmdebuginfo.patch
# generic releng plugins that can be used to build plugins
# see this thread for details: 
# https://www.redhat.com/archives/fedora-devel-java-list/2006-April/msg00048.html
# This needs to be submitted upstream
Patch15:        %{name}-pde.build-add-package-build.patch
# This tomcat stuff will change when they move to the equinox jetty provider
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=98371
Patch6:         %{name}-tomcat55.patch
Patch7:         %{name}-tomcat55-build.patch
Patch8:         %{name}-webapp-tomcat55.patch
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=90630
Patch5:         %{name}-updatehomedir.patch
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=161996
Patch9:         %{name}-ecj-square-bracket-classpath.patch
# Use ecj for gcj
Patch17:        %{name}-ecj-gcj.patch
# Build against firefox:
#  - fix swt profile include path
#  - don't compile the mozilla 1.7 / firefox profile library -- build it inline
#  - don't use symbols not in our firefox builds
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=161310
# FIXME:  these can probably go away >= 3.3M4
# Note:  I made this patch from within Eclipse and then did the following to
#        it due to spaces in the paths:
#  sed --in-place "s/Eclipse\ SWT\ Mozilla/Eclipse_SWT_Mozilla/g" eclipse-swt-firefox.patch
#  sed --in-place "s/Eclipse\ SWT\ PI/Eclipse_SWT_PI/g" eclipse-swt-firefox.patch
Patch18:        %{name}-swt-firefox.patch
Patch19:        %{name}-swt-firefox.2.patch
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=209393
# http://gcc.gnu.org/bugzilla/show_bug.cgi?id=29853
Patch20:        %{name}-workaround-plugin.xml-parsing-bug-gcc-bz29853.patch
# This is already upstream in 3.3 builds.  It *may* get into 3.2.2.
Patch21:        customBuildCallbacks.xml-add-pre.gather.bin.parts.patch
# Add ppc64 to the list of archs with gre64.conf
# part of https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=207016
Patch22:        %{name}-ppc64gre64.patch
# This patch allowed us to remove
# /usr/share/eclipse/configuration/org.eclipse.update/platform.xml -- which
# fixed a number of update-related bugs -- in an FC6 update.
# We can remove this patch for Fedora 8.
Patch23:        %{name}-launcher-addplatformtotildeeclipse.patch
Patch24:        %{name}-add-ppc64-sparc64-s390-s390x.patch
Patch25:        %{name}-osgi-Java-1.7-profile.patch
Patch100:       %{name}-libswt-model.patch
Patch101:       %{name}-ssh.patch
Patch201:       %{name}-nativepresentation.patch
Patch202:       %{name}-disable-motif.patch
Patch203:       %{name}-disable-javadoc.patch
Patch204:       %{name}-gjdoc-reflection.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  ant
BuildRequires:  jpackage-utils >= 0:1.5, make, gcc
BuildRequires:  gnome-vfs2-devel
BuildRequires:  gtk2-devel
BuildRequires:  glib2-devel
BuildRequires:  libgnome2-devel
BuildRequires:  libgnomeui2-devel
BuildRequires:  gcc-c++
BuildRequires:  mozilla-firefox
BuildRequires:  mozilla-firefox-devel
BuildRequires:  nspr-devel
BuildRequires:  libxtst-devel
BuildRequires:  mesagl-devel
BuildRequires:  mesaglu-devel
BuildRequires:  cairo-devel >= 0:1.0
BuildRequires:  unzip
BuildRequires:  java-javadoc
BuildRequires:  desktop-file-utils
BuildRequires:  gcc%gccsuffix-c++
%if %{gcj_support}
BuildRequires:  gcc%gccsuffix-java >= 0:4.1.2
BuildRequires:  java-gcj-compat-devel >= 0:1.0.64
BuildRequires:  gjdoc >= 0:0.7.7
%else
BuildRequires:  java-1.4.2-gcj-compat-devel >= 0:1.4.2
%endif

# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=180642
BuildRequires: ant-antlr ant-apache-bcel ant-apache-bsf ant-apache-log4j ant-apache-oro ant-apache-regexp ant-apache-resolver ant-commons-logging
BuildRequires: ant-commons-net ant-jmf
BuildRequires: ant-javamail ant-jdepend ant-junit ant-nodeps ant-swing ant-trax ant-jsch
BuildRequires: jsch >= 0:0.1.28-1jpp
BuildRequires: jakarta-commons-beanutils jakarta-commons-collections jakarta-commons-digester jakarta-commons-dbcp jakarta-commons-el jakarta-commons-fileupload jakarta-commons-launcher jakarta-commons-logging jakarta-commons-modeler jakarta-commons-pool
BuildRequires: mx4j >= 0:2.1
BuildRequires: tomcat5 >= %{tomcatepoch}:%{tomcatversion}
BuildRequires: tomcat5-jasper >= %{tomcatepoch}:%{tomcatversion}
BuildRequires: tomcat5-servlet-2.4-api >= %{tomcatepoch}:%{tomcatversion}
BuildRequires: lucene
BuildRequires: lucene-demo
BuildRequires: lucene-src
BuildRequires: regexp 
BuildRequires: junit junit4
%if %{gcj_support}
Requires(post):   java-gcj-compat >= 0:1.0.64
Requires(postun): java-gcj-compat >= 0:1.0.64
%endif
#BuildRequires: icu4j

%description
The Eclipse Platform is designed for building integrated development
environments (IDEs) that can be used to create applications as diverse
as web sites, embedded Java(tm) programs, C++ programs, and Enterprise
JavaBeans(tm).

%package        ecj
Summary:        Eclipse Compiler for Java
Group:          Development/Java
Obsoletes:      ecj < 3.2.0
Provides:       ecj = %{epoch}:%{version}-%{release}
%if %{gcj_support}
Requires(post):   java-gcj-compat >= 0:1.0.64
Requires(postun): java-gcj-compat >= 0:1.0.64
%else
Requires:       java >= 0:1.4.2
%endif

%description    ecj
Eclipse compiler for Java.

%package     -n %{libname}-gtk2
Summary:        SWT Library for GTK+-2.0
Group:          Development/Java
%if %{gcj_support}
Requires(post):   java-gcj-compat >= 0:1.0.64
Requires(postun): java-gcj-compat >= 0:1.0.64
%endif
Requires:       %mklibname mozilla-firefox %{firefox_version}

%description -n %{libname}-gtk2
SWT Library for GTK+-2.0.

%package        rcp
Summary:        Eclipse Rich Client Platform
Group:          Development/Java
Requires:       %{libname}-gtk2 = %{epoch}:%{version}-%{release}
# This file-level requirement is for the bi-arch multilib case
%if 0
Requires:       %{_libdir}/%{name}/plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}_3.2.2.v3236.jar
%endif
Requires(post):     %{libname}-gtk2 = %{epoch}:%{version}-%{release}
Requires(postun):   %{libname}-gtk2 = %{epoch}:%{version}-%{release}
%if %{gcj_support}
Requires(post):     java-gcj-compat >= 0:1.0.64
Requires(postun):   java-gcj-compat >= 0:1.0.64
%else
Requires:       java >= 0:1.4.2
%endif

%description    rcp
Eclipse Rich Client Platform

%package        rcp-sdk
Summary:        Eclipse Rich Client Platform SDK
Group:          Development/Java
Requires:       %{name}-rcp = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-rcp = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-rcp = %{epoch}:%{version}-%{release}

%description    rcp-sdk
Source for Eclipse Rich Client Platform for use within Eclipse.

%package        platform
Summary:        Eclipse platform common files
Group:          Development/Java
Provides:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-ui %{name}-gtk2 %{name}-scripts eclipse
Provides:       %{name}-ui = %{epoch}:%{version}-%{release}
Provides:       %{name}-scripts = %{epoch}:%{version}-%{release}
Provides:       %{name}-gtk2 = %{epoch}:%{version}-%{release}
%if %{gcj_support}
Requires:       java-gcj-compat >= 0:1.0.64
Requires(post):   java-gcj-compat >= 0:1.0.64
Requires(postun): java-gcj-compat >= 0:1.0.64
%else
Requires:       java >= 0:1.4.2
%endif
Requires:       %{name}-rcp = %{epoch}:%{version}-%{release}
Requires(post):   %{name}-rcp = %{epoch}:%{version}-%{release}
Requires(postun): %{name}-rcp = %{epoch}:%{version}-%{release}
Requires: %{libname}-gtk2 = %{epoch}:%{version}-%{release}
Requires: %mklibname mozilla-firefox %{firefox_version}
Requires: ant-antlr ant-apache-bcel ant-apache-bsf ant-apache-log4j ant-apache-oro ant-apache-regexp ant-apache-resolver ant-commons-logging
Requires: ant-commons-net ant-jmf
Requires: ant-javamail ant-jdepend ant-junit ant-nodeps ant-swing ant-trax ant-jsch
Requires: jakarta-commons-beanutils jakarta-commons-collections jakarta-commons-digester jakarta-commons-dbcp jakarta-commons-el jakarta-commons-fileupload jakarta-commons-launcher jakarta-commons-logging jakarta-commons-modeler jakarta-commons-pool
Requires: mx4j >= 0:2.1
Requires: tomcat5 >= %{tomcatepoch}:%{tomcatversion}
Requires: tomcat5-jasper >= %{tomcatepoch}:%{tomcatversion}
Requires: tomcat5-servlet-2.4-api >= %{tomcatepoch}:%{tomcatversion}
Requires: lucene lucene-demo lucene-src 
Requires: regexp
Requires: junit junit4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description    platform
The Eclipse Platform is the base of all IDE plugins.  This does not include the
Java Development Tools or the Plugin Development Environment.

%package        platform-sdk
Summary:        Eclipse Platform SDK
Group:          Development/Java
Requires:       %{name}-platform = %{epoch}:%{version}-%{release}
Requires:       %{name}-rcp-sdk = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-platform = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-platform = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-rcp-sdk = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-rcp-sdk = %{epoch}:%{version}-%{release}

%description    platform-sdk
Source and docs for Eclipse Platform for use within Eclipse.

%package        jdt
Summary:        Eclipse Java Development Tools
Group:          Development/Java
Requires:       %{name}-platform = %{epoch}:%{version}-%{release}
Requires:       %{name}-ecj = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-platform = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-platform = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-ecj = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-ecj = %{epoch}:%{version}-%{release}
Requires:       junit junit4
Requires:       java-javadoc
%if %{gcj_support}
Requires(post):   java-gcj-compat >= 0:1.0.64
Requires(postun): java-gcj-compat >= 0:1.0.64
%endif

%description    jdt
Eclipse Java Development Tools.  This package is required to use Eclipse for
developing software written in the Java programming language.

%package        jdt-sdk
Summary:        Eclipse Java Development Tools SDK
Group:          Development/Java
Requires:       %{name}-jdt = %{epoch}:%{version}-%{release}
Requires:       %{name}-platform-sdk = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-jdt = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-jdt = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-platform-sdk = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-platform-sdk = %{epoch}:%{version}-%{release}

%description    jdt-sdk
Source and docs for Eclipse Java Development Tools for use within Eclipse.

%package        pde
Summary:        Eclipse Plugin Development Environment
Group:          Development/Java
Requires:       %{name}-jdt = %{epoch}:%{version}-%{release}
Requires:       %{name}-pde-runtime = %{epoch}:%{version}-%{release}
Requires:       %{name}-platform-sdk = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-jdt = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-jdt = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-pde-runtime = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-pde-runtime = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-platform-sdk = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-platform-sdk = %{epoch}:%{version}-%{release}
%if %{gcj_support}
Requires(post):   java-gcj-compat >= 0:1.0.64
Requires(postun): java-gcj-compat >= 0:1.0.64
%endif

%description    pde
Eclipse Plugin Development Environment.  This package is required for
developing Eclipse plugins.

%package        pde-runtime
Summary:        Eclipse Plugin Development Environment runtime plugin
Group:          Development/Java
Requires:       %{name}-jdt = %{epoch}:%{version}-%{release}
Requires:       %{name}-platform = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-platform = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-platform = %{epoch}:%{version}-%{release}
%if %{gcj_support}
Requires(post):   java-gcj-compat >= 0:1.0.64
Requires(postun): java-gcj-compat >= 0:1.0.64
%endif

%description    pde-runtime
Eclipse Plug-in Development Environment runtime plugin
(org.eclipse.pde.runtime).

%package        pde-sdk
Summary:        Eclipse Plugin Development Environment SDK
Group:          Development/Java
Requires:       %{name}-pde = %{epoch}:%{version}-%{release}
Requires:       %{name}-jdt-sdk = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-pde = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-pde = %{epoch}:%{version}-%{release}

%description    pde-sdk
Source and docs for Eclipse Plugin Development Environment for use within
Eclipse.

%package        sdk
Summary:        Eclipse SDK
Group:          Development/Java
Requires:       %{name}-platform-sdk = %{epoch}:%{version}-%{release}
Requires:       %{name}-jdt-sdk = %{epoch}:%{version}-%{release}
Requires:       %{name}-pde-sdk = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-platform-sdk = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-platform-sdk = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-pde-sdk = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-pde-sdk = %{epoch}:%{version}-%{release}
Requires(post):    %{name}-jdt-sdk = %{epoch}:%{version}-%{release}
Requires(postun):  %{name}-jdt-sdk = %{epoch}:%{version}-%{release}
%if 0
# This file requirement is to deal with the biarch installation case
Requires(post):    %{_libdir}/%{name}/configuration/config.ini
Requires(postun):  %{_libdir}/%{name}/configuration/config.ini
%else
Requires(post):    eclipse-rcp
Requires(postun):  eclipse-rcp
%endif
%if %{gcj_support}
Requires(post):    java-gcj-compat >= 0:1.0.64
Requires(postun):  java-gcj-compat >= 0:1.0.64
%endif

%description    sdk
The Eclipse SDK.  This package is similar to a meta-package which brings in
the Eclipse Platform SDK, the Eclipse Java Development Tools SDK, and the
Eclipse Plugin Development Environment SDK.  It also contains the
org.eclipse.sdk plugin and feature.  This package is only needed if you intend
to create Eclipse applications.

%prep
%setup -q -c

%patch0 -p0
sed --in-place "s/java5.home/java.home/" build.xml
%patch2 -p0
%patch3 -p0
# FIXME:  investigate why we are pushd'ing here
# Build swttools.jar
pushd plugins/org.eclipse.swt.gtk.linux.x86_64
%patch4 -p0
popd
%patch5 -p0

# tomcat patches
pushd plugins/org.eclipse.tomcat
%patch6 -p0
%patch7 -p0
popd
sed --in-place "s/4.1.130/%{tomcatversion}/g"           \
                features/org.eclipse.platform/build.xml \
                plugins/org.eclipse.tomcat/build.xml    \
                plugins/org.eclipse.tomcat/META-INF/MANIFEST.MF   \
                assemble.*.xml
pushd plugins/org.eclipse.help.webapp
%patch8 -p0
popd

pushd plugins/org.eclipse.jdt.core
%patch9 -p0
%patch17 -p0
popd
%patch11 -p0

# Because the launcher source is zipped up, we need to unzip, patch, and re-pack
# FIXME: figure out why we need to patch and sed twice and fix upstream
mkdir launchertmp
unzip -qq -d launchertmp plugins/org.eclipse.platform/launchersrc.zip
pushd launchertmp
%patch12 -p0
%patch22 -p0
%patch23 -p0
# put the configuration directory in an arch-specific location
sed --in-place "s:/usr/lib/eclipse/configuration:%{_libdir}/%{name}/configuration:" library/eclipse.c
# make the eclipse binary relocatable
sed --in-place "s:/usr/share/eclipse:%{_datadir}/%{name}:" library/eclipse.c
zip -q -9 -r ../launchersrc.zip *
popd
mv launchersrc.zip plugins/org.eclipse.platform
rm -r launchertmp
pushd features/org.eclipse.platform.launchers
%patch12 -p0
%patch22 -p0
%patch23 -p0

# put the configuration directory in an arch-specific location
sed --in-place "s:/usr/lib/eclipse:%{_libdir}/%{name}:" library/eclipse.c
# make the eclipse binary relocatable
sed --in-place "s:/usr/share/eclipse:%{_datadir}/%{name}:" library/eclipse.c
popd

# use our system-installed javadocs
sed --in-place "s|http://java.sun.com/j2se/1.4.2/docs/api|%{_javadocdir}/java|" \
   plugins/org.eclipse.platform.doc.isv/platformOptions.txt
sed --in-place "s|http://java.sun.com/j2se/1.5/docs/api|%{_javadocdir}/java|" \
   plugins/org.eclipse.jdt.doc.isv/jdtaptOptions.txt                     \
   plugins/org.eclipse.jdt.doc.isv/jdtOptions.txt
sed --in-place "s|http://java.sun.com/j2se/1.4/docs/api|%{_javadocdir}/java|" \
   plugins/org.eclipse.pde.doc.user/pdeOptions.txt                       \
   plugins/org.eclipse.pde.doc.user/pdeOptions
%patch14 -p0

pushd plugins/org.eclipse.pde.build
%patch15
sed --in-place "s:/usr/share/eclipse:%{_datadir}/%{name}:" templates/package-build/build.properties
popd

# Build against our firefox packages
pushd plugins/org.eclipse.swt
mv "Eclipse SWT Mozilla" Eclipse_SWT_Mozilla
mv "Eclipse SWT PI" Eclipse_SWT_PI
%patch18
mv Eclipse_SWT_Mozilla "Eclipse SWT Mozilla"
mv Eclipse_SWT_PI "Eclipse SWT PI"
popd
pushd plugins/org.eclipse.swt.tools
mv "JNI Generation" JNI_Generation
%patch19
mv JNI_Generation "JNI Generation"
popd

# workaround for GNU XML bug when parsing plugin.xml
# http://gcc.gnu.org/bugzilla/show_bug.cgi?id=29853
pushd plugins/org.eclipse.pde.core
%patch20
popd

# customcallbacks fixes.  They are upstream already.
pushd plugins/org.eclipse.platform.doc.isv
%patch21 -p0
popd
pushd plugins/org.eclipse.platform.doc.user
%patch21 -p0
popd

pushd plugins/org.eclipse.osgi
%patch25 -p0
popd

# Splashscreen
%if 0
pushd plugins/org.eclipse.platform
cp %{SOURCE11} splash.bmp
popd
%endif

# FIXME this should be patched upstream with a flag to turn on and off 
# all output should be directed to stdout
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=144942
find -type f -name \*.xml -exec sed --in-place -r "s/output=\".*(txt|log).*\"//g" "{}" \;

# Remove existing .sos
find -name \*.so | xargs rm

# Symlinks
# FIXME: link in icu4j
## BEGIN ANT ##
rm plugins/org.apache.ant/lib/ant-antlr.jar
rm plugins/org.apache.ant/lib/ant-antlrsrc.zip
rm plugins/org.apache.ant/lib/ant-apache-bcel.jar
rm plugins/org.apache.ant/lib/ant-apache-bcelsrc.zip
rm plugins/org.apache.ant/lib/ant-apache-bsf.jar
rm plugins/org.apache.ant/lib/ant-apache-bsfsrc.zip
rm plugins/org.apache.ant/lib/ant-apache-log4j.jar
rm plugins/org.apache.ant/lib/ant-apache-log4jsrc.zip
rm plugins/org.apache.ant/lib/ant-apache-oro.jar
rm plugins/org.apache.ant/lib/ant-apache-orosrc.zip
rm plugins/org.apache.ant/lib/ant-apache-regexp.jar
rm plugins/org.apache.ant/lib/ant-apache-regexpsrc.zip
rm plugins/org.apache.ant/lib/ant-apache-resolver.jar
rm plugins/org.apache.ant/lib/ant-apache-resolversrc.zip
rm plugins/org.apache.ant/lib/ant-commons-logging.jar
rm plugins/org.apache.ant/lib/ant-commons-loggingsrc.zip
rm plugins/org.apache.ant/lib/ant-commons-net.jar
rm plugins/org.apache.ant/lib/ant-commons-netsrc.zip
rm plugins/org.apache.ant/lib/ant-icontract.jar
rm plugins/org.apache.ant/lib/ant-icontractsrc.zip
rm plugins/org.apache.ant/lib/ant-jai.jar
rm plugins/org.apache.ant/lib/ant-jaisrc.zip
rm plugins/org.apache.ant/lib/ant.jar
rm plugins/org.apache.ant/lib/antsrc.zip
rm plugins/org.apache.ant/lib/ant-javamail.jar
rm plugins/org.apache.ant/lib/ant-javamailsrc.zip
rm plugins/org.apache.ant/lib/ant-jdepend.jar
rm plugins/org.apache.ant/lib/ant-jdependsrc.zip
rm plugins/org.apache.ant/lib/ant-jmf.jar
rm plugins/org.apache.ant/lib/ant-jmfsrc.zip
rm plugins/org.apache.ant/lib/ant-jsch.jar
rm plugins/org.apache.ant/lib/ant-jschsrc.zip
rm plugins/org.apache.ant/lib/ant-junit.jar
rm plugins/org.apache.ant/lib/ant-junitsrc.zip
rm plugins/org.apache.ant/lib/ant-launcher.jar
rm plugins/org.apache.ant/lib/ant-launchersrc.zip
rm plugins/org.apache.ant/lib/ant-netrexx.jar
rm plugins/org.apache.ant/lib/ant-netrexxsrc.zip
rm plugins/org.apache.ant/lib/ant-nodeps.jar
rm plugins/org.apache.ant/lib/ant-nodepssrc.zip
rm plugins/org.apache.ant/lib/ant-starteam.jar
rm plugins/org.apache.ant/lib/ant-starteamsrc.zip
rm plugins/org.apache.ant/lib/ant-stylebook.jar
rm plugins/org.apache.ant/lib/ant-stylebooksrc.zip
rm plugins/org.apache.ant/lib/ant-swing.jar
rm plugins/org.apache.ant/lib/ant-swingsrc.zip
rm plugins/org.apache.ant/lib/ant-trax.jar
rm plugins/org.apache.ant/lib/ant-traxsrc.zip
rm plugins/org.apache.ant/lib/ant-vaj.jar
rm plugins/org.apache.ant/lib/ant-vajsrc.zip
rm plugins/org.apache.ant/lib/ant-weblogic.jar
rm plugins/org.apache.ant/lib/ant-weblogicsrc.zip
rm plugins/org.apache.ant/lib/ant-xalan1.jar
rm plugins/org.apache.ant/lib/ant-xalan1src.zip
rm plugins/org.apache.ant/lib/ant-xslp.jar
rm plugins/org.apache.ant/lib/ant-xslpsrc.zip
# FIXME:  use build-jar-repository
ln -s %{_javadir}/ant/ant-antlr.jar plugins/org.apache.ant/lib/ant-antlr.jar
ln -s %{_javadir}/ant/ant-apache-bcel.jar plugins/org.apache.ant/lib/ant-apache-bcel.jar
ln -s %{_javadir}/ant/ant-apache-bsf.jar plugins/org.apache.ant/lib/ant-apache-bsf.jar
ln -s %{_javadir}/ant/ant-apache-log4j.jar plugins/org.apache.ant/lib/ant-apache-log4j.jar
ln -s %{_javadir}/ant/ant-apache-oro.jar plugins/org.apache.ant/lib/ant-apache-oro.jar
ln -s %{_javadir}/ant/ant-apache-regexp.jar plugins/org.apache.ant/lib/ant-apache-regexp.jar
ln -s %{_javadir}/ant/ant-apache-resolver.jar plugins/org.apache.ant/lib/ant-apache-resolver.jar
ln -s %{_javadir}/ant/ant-commons-logging.jar plugins/org.apache.ant/lib/ant-commons-logging.jar
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=180642
# the symlinks that are commented-out are not currently shipped on Fedora
ln -s %{_javadir}/ant/ant-commons-net.jar plugins/org.apache.ant/lib/ant-commons-net.jar
#ln -s %{_javadir}/ant/ant-icontract.jar plugins/org.apache.ant/lib/ant-icontract.jar
#ln -s %{_javadir}/ant/ant-jai.jar plugins/org.apache.ant/lib/ant-jai.jar
ln -s %{_javadir}/ant.jar plugins/org.apache.ant/lib/ant.jar
ln -s %{_javadir}/ant/ant-javamail.jar plugins/org.apache.ant/lib/ant-javamail.jar
ln -s %{_javadir}/ant/ant-jdepend.jar plugins/org.apache.ant/lib/ant-jdepend.jar
ln -s %{_javadir}/ant/ant-jmf.jar plugins/org.apache.ant/lib/ant-jmf.jar
ln -s %{_javadir}/ant/ant-jsch.jar plugins/org.apache.ant/lib/ant-jsch.jar
ln -s %{_javadir}/ant/ant-junit.jar plugins/org.apache.ant/lib/ant-junit.jar
ln -s %{_javadir}/ant-launcher.jar plugins/org.apache.ant/lib/ant-launcher.jar
#ln -s %{_javadir}/ant/ant-netrexx.jar plugins/org.apache.ant/lib/ant-netrexx.jar
ln -s %{_javadir}/ant/ant-nodeps.jar plugins/org.apache.ant/lib/ant-nodeps.jar
#ln -s %{_javadir}/ant/ant-starteam.jar plugins/org.apache.ant/lib/ant-starteam.jar
#ln -s %{_javadir}/ant/ant-stylebook.jar plugins/org.apache.ant/lib/ant-stylebook.jar
ln -s %{_javadir}/ant/ant-swing.jar plugins/org.apache.ant/lib/ant-swing.jar
ln -s %{_javadir}/ant/ant-trax.jar plugins/org.apache.ant/lib/ant-trax.jar
#ln -s %{_javadir}/ant/ant-vaj.jar plugins/org.apache.ant/lib/ant-vaj.jar
#ln -s %{_javadir}/ant/ant-weblogic.jar plugins/org.apache.ant/lib/ant-weblogic.jar
#ln -s %{_javadir}/ant/ant-xalan1.jar plugins/org.apache.ant/lib/ant-xalan1.jar
#ln -s %{_javadir}/ant/ant-xslp.jar plugins/org.apache.ant/lib/ant-xslp.jar
## END ANT ##

## BEGIN LUCENE ##
rm plugins/org.apache.lucene/lucene-1.4.3.jar
rm plugins/org.apache.lucene/lucene-1.4.3-src.zip
ln -s %{_datadir}/lucene/lucene-src.zip plugins/org.apache.lucene/lucene-1.4.3-src.zip
ln -s %{_datadir}/lucene/lucene-demos.jar plugins/org.apache.lucene/parser.jar
ln -s %{_javadir}/lucene.jar plugins/org.apache.lucene/lucene-1.4.3.jar
## END LUCENE ##

## BEGIN TOMCAT ##
rm plugins/org.eclipse.tomcat/commons-beanutils.jar
rm plugins/org.eclipse.tomcat/commons-collections.jar
rm plugins/org.eclipse.tomcat/commons-digester.jar
rm plugins/org.eclipse.tomcat/commons-logging-api.jar
rm plugins/org.eclipse.tomcat/commons-modeler.jar
rm plugins/org.eclipse.tomcat/jakarta-regexp-1.3.jar
rm plugins/org.eclipse.tomcat/servlet.jar
rm plugins/org.eclipse.tomcat/servlets-manager.jar
rm plugins/org.eclipse.tomcat/naming-common.jar
rm plugins/org.eclipse.tomcat/servlets-common.jar
rm plugins/org.eclipse.tomcat/tomcat-http11.jar
rm plugins/org.eclipse.tomcat/bootstrap.jar
rm plugins/org.eclipse.tomcat/catalina.jar
rm plugins/org.eclipse.tomcat/jasper-compiler.jar
rm plugins/org.eclipse.tomcat/jasper-runtime.jar
rm plugins/org.eclipse.tomcat/mx4j-jmx.jar
rm plugins/org.eclipse.tomcat/naming-resources.jar
rm plugins/org.eclipse.tomcat/naming-factory.jar
rm plugins/org.eclipse.tomcat/servlets-default.jar
rm plugins/org.eclipse.tomcat/servlets-invoker.jar
rm plugins/org.eclipse.tomcat/tomcat-coyote.jar
rm plugins/org.eclipse.tomcat/tomcat-util.jar
mkdir -p plugins/org.eclipse.tomcat/lib
ln -s %{tomcatsharedir}/bin/bootstrap.jar plugins/org.eclipse.tomcat/lib/bootstrap.jar
ln -s %{tomcatlibdir}/server/lib/catalina.jar plugins/org.eclipse.tomcat/lib/catalina.jar
ln -s %{tomcatlibdir}/server/lib/catalina-optional.jar plugins/org.eclipse.tomcat/lib/catalina-optional.jar
ln -s %{_javadir}/jasper5-compiler.jar plugins/org.eclipse.tomcat/lib/jasper-compiler.jar
ln -s %{_javadir}/jasper5-runtime.jar plugins/org.eclipse.tomcat/lib/jasper-runtime.jar
ln -s %{_javadir}/mx4j/mx4j.jar plugins/org.eclipse.tomcat/lib/mx4j.jar
ln -s %{_javadir}/mx4j/mx4j-impl.jar plugins/org.eclipse.tomcat/lib/mx4j-impl.jar
ln -s %{_javadir}/mx4j/mx4j-jmx.jar plugins/org.eclipse.tomcat/lib/mx4j-jmx.jar
ln -s %{tomcatlibdir}/common/lib/naming-factory.jar plugins/org.eclipse.tomcat/lib/naming-factory.jar
ln -s %{tomcatlibdir}/common/lib/naming-resources.jar plugins/org.eclipse.tomcat/lib/naming-resources.jar
ln -s %{tomcatlibdir}/server/lib/servlets-default.jar plugins/org.eclipse.tomcat/lib/servlets-default.jar
ln -s %{tomcatlibdir}/server/lib/servlets-invoker.jar plugins/org.eclipse.tomcat/lib/servlets-invoker.jar
ln -s %{tomcatlibdir}/server/lib/tomcat-coyote.jar plugins/org.eclipse.tomcat/lib/tomcat-coyote.jar
ln -s %{tomcatlibdir}/server/lib/tomcat-http.jar plugins/org.eclipse.tomcat/lib/tomcat-http.jar
ln -s %{tomcatlibdir}/server/lib/tomcat-util.jar plugins/org.eclipse.tomcat/lib/tomcat-util.jar
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-beanutils
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-collections
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-dbcp
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-digester
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-digester-rss
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-el
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-fileupload
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-launcher
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-logging-api
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-modeler
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib commons-pool
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib jspapi
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib regexp
build-jar-repository -s -p plugins/org.eclipse.tomcat/lib servletapi5
## END TOMCAT ##

build-jar-repository -s -p plugins/org.junit junit

rm plugins/org.junit4/junit-4.1.jar
ln -s %{_javadir}/junit4.jar plugins/org.junit4/junit-4.1.jar

pushd plugins/org.eclipse.swt/Eclipse\ SWT\ PI/gtk/library
# /usr/lib -> /usr/lib64
sed --in-place "s:/usr/lib/:%{_libdir}/:g" build.sh
sed --in-place "s:-L\$(AWT_LIB_PATH):-L%{java_home}/jre/lib/%{_arch}:" make_linux.mak
popd

# FIXME: figure out what's going on with build.index.
find plugins -type f -name \*.xml -exec sed --in-place "s/\(<antcall target=\"build.index\".*\/>\)/<\!-- \1 -->/" "{}" \;

# the swt version is set to HEAD on ia64 but shouldn't be
# get swt version
SWT_MAJ_VER=$(grep maj_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_MIN_VER=$(grep min_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_VERSION=$SWT_MAJ_VER$SWT_MIN_VER
swt_frag_ver=$(grep v$SWT_VERSION plugins/org.eclipse.swt.gtk.linux.x86/build.xml | sed "s:.*<.*\"\(.*\)\"/>:\1:")
swt_frag_ver_ia64=$(grep "version\.suffix\" value=" plugins/org.eclipse.swt.gtk.linux.ia64/build.xml | sed "s:.*<.*\"\(.*\)\"/>:\1:")
sed --in-place "s/$swt_frag_ver_ia64/$swt_frag_ver/g" plugins/org.eclipse.swt.gtk.linux.ia64/build.xml \
                                                      assemble.org.eclipse.sdk.linux.gtk.ia64.xml \
                                                      features/org.eclipse.rcp/build.xml

## Nasty hack to get suppport for ppc64, s390{,x} and sparc{,64}
%patch24 -p0

pushd './plugins/org.eclipse.swt/Eclipse SWT PI/gtk/library'
%patch100 -p0
popd
%patch101 -p1

%patch201 -p1
%patch202 -p1
%patch203 -p1
%patch204 -p1

%{__sed} --in-place 's,^JAVA_HOME =.*,JAVA_HOME = %{java_home},' plugins/org.eclipse.core.filesystem/natives/unix/linux/Makefile

# (anssi) JNIGenerator fails to run with
# [java] java.lang.NoClassDefFoundError: java.security.Security
# thus leaving ia64 and x86_64 with 32bit-only C source code.
# Setting fork="yes" seems to fix it. jvm is used to ensure correct
# jvm in fork mode.
%{__sed} --in-place 's,<java ,<java fork="true" jvm="%{java}" ,' plugins/org.eclipse.*/build.xml
%{__sed} --in-place 's,<java ,<java jvm="%{java}" ,' build.xml

# there is only partial support for ppc64 in 3.2 so we have to remove this 
# partial support to get the replacemnt hack to work
find -name \*ppc64\* | xargs rm -r
# remove ppc64 support from features/org.eclipse.platform.source/feature.xml
# replace ppc64 with a fake arch (ppc128) so we don't have duplicate ant targets
find -type f -name \*.xml -exec sed --in-place "s/\(rootFileslinux_gtk_\)ppc64/\1ppc128/g" "{}" \;
# remove org.eclipse.platform.source.linux.gtk.ppc64,3.2.0.v20060602-0010-gszCh-8eOaU1uKq
sed --in-place "s/,.\{38\}ppc64.*macosx/,org.eclipse.platform.source.macosx/g" features/org.eclipse.platform.source/build.xml
# replace final occurances with an existing arch
sed --in-place "s/ppc64/x86_64/g" features/org.eclipse.platform.source/build.xml
# Move all of the ia64 directories to ppc64 or s390{,x} or sparc{,64} dirs and replace 
# the ia64 strings with ppc64 or s390(x)
%ifarch ppc64 s390 s390x %{sunsparc}
  for f in $(find -name \*ia64\* | grep -v motif | grep -v ia64_32); do 
    mv $f $(echo $f | sed "s/ia64/%{_arch}/")
  done
  find -type f ! -name \*.java -a ! -name feature.xml -exec sed --in-place "s/ia64_32/@eye-eh-64_32@/g" "{}" \;
  find -type f ! -name \*.java -a ! -name feature.xml -exec sed --in-place "s/ia64/%{_arch}/g" "{}" \;
  find -type f ! -name \*.java -a ! -name feature.xml -exec sed --in-place "s/@eye-eh-64_32@/ia64_32/g" "{}" \;
%endif 

%if 0
# link to the jsch jar
rm baseLocation/plugins/com.jcraft.jsch_0.1.28.jar
ln -s %{_javadir}/jsch.jar baseLocation/plugins/com.jcraft.jsch_0.1.28.jar
%endif

# set the icu4j plugins for building
pushd baseLocation/plugins
rm com.ibm.icu.base_3.4.5.20061213.jar \
   com.ibm.icu_3.4.5.20061213.jar \
   com.ibm.icu.base.source_3.4.5.20061213/src/com.ibm.icu.base_3.4.5.20061213/src.zip \
   com.ibm.icu.source_3.4.5.20061213/src/com.ibm.icu_3.4.5.20061213/src.zip
mkdir -p icu4j-build-temp

pushd icu4j-build-temp
unzip -qq %{SOURCE7} 
sed --in-place "s/ .*bootclasspath=.*//g" build.xml
ant eclipseProjects
popd

mkdir -p icu4j-build
mv icu4j-build-temp/eclipseProjects/com.ibm.icu icu4j-build
mv icu4j-build-temp/eclipseProjects/com.ibm.icu.base icu4j-build
rm -r icu4j-build-temp

# add build.xml patches
pushd icu4j-build
%patch1 -p1
popd 

popd

# delete included jars
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=170662
rm plugins/org.eclipse.swt.win32.win32.x86/swt.jar \
   plugins/org.eclipse.swt/extra_jars/exceptions.jar \
   plugins/org.eclipse.swt.tools/swttools.jar \
   features/org.eclipse.platform.launchers/bin/startup.jar \
   plugins/org.eclipse.team.cvs.ssh2/com.jcraft.jsch_*.jar

# make sure there are no jars left
JARS=""
for j in $(find -name \*.jar ! -name 'com.jcraft.jsch_0.1.28.jar'); do
  if [ ! -L $j ]; then
    JARS="$JARS $j"
  fi
done
if [ ! -z "$JARS" ]; then
    echo "These jars should be deleted and symlinked to system jars: $JARS"
    exit 1
fi

tar jxf %{SOURCE20}

%build
env
ORIGCLASSPATH=$CLASSPATH

# (anssi) build with the same version of gcc as gcj
export CC=gcc%{gccsuffix}
export CXX=g++%{gccsuffix}

# (anssi) and of course the gcc is hardcoded at some points of the build...
mkdir -p gcc_to_use
ln -sf $(which $CC) gcc_to_use/gcc
ln -sf $(which $CXX) gcc_to_use/g++
export PATH=$(pwd)/gcc_to_use:$PATH

%if 1
# Build jsch
pushd baseLocation/plugins
# extract the Manifest file
unzip -qq -o -d com.jcraft.jsch_0.1.28.jar-build com.jcraft.jsch_*.jar -x com\*
rm com.jcraft.jsch_*.jar
popd
# FIXME jar -V does not work for proprietary VMs 
pushd baseLocation/plugins/com.jcraft.jsch_0.1.28.jar-build
unzip -qq %{_javadir}/jsch.jar -x META-INF\*
sed --in-place "s/$(grep Created-By: META-INF/MANIFEST.MF)/Created-By: $(jar -V | head -1)/" META-INF/MANIFEST.MF
jar -Mcf ../com.jcraft.jsch_0.1.28.jar *
popd
# FIXME don't delete this, do what icu4j does
rm -r baseLocation/plugins/com.jcraft.jsch_0.1.28.jar-build
%endif

# Finish the icu4j build
pushd baseLocation/plugins

# Build the icu.base plugin
zipfile=$PWD/com.ibm.icu.base.source_3.4.5.20061213/src/com.ibm.icu.base_3.4.5.20061213/src.zip
pushd icu4j-build/com.ibm.icu.base/src
find -name \*.java | xargs touch --date=1/1/1980
zip -X -9 -r $zipfile . -i \*.java
popd
pushd icu4j-build/com.ibm.icu.base
%{ant} build.update.jar
popd
mv icu4j-build/com.ibm.icu.base/com.ibm.icu.base_3.4.5.jar com.ibm.icu.base_3.4.5.20061213.jar

# Build the icu plugin
zipfile=$PWD/com.ibm.icu.source_3.4.5.20061213/src/com.ibm.icu_3.4.5.20061213/src.zip
pushd icu4j-build/com.ibm.icu/src
find -name \*.java | xargs touch --date=1/1/1980
zip -X -9 -r $zipfile . -i \*.java
popd
pushd icu4j-build/com.ibm.icu
%{ant} build.update.jar
popd
mv icu4j-build/com.ibm.icu/com.ibm.icu_3.4.5.jar com.ibm.icu_3.4.5.20061213.jar

popd

# Bootstrapping is 3 parts:
# 1. Build ecj with gcj -C -- only necessary until gcjx/ecj lands in gcc
# 2. Build ecj with gcj-built ecj ("javac")
# 3. Re-build ecj with output of 2.

%if %{gcj_support}
  # Unzip the "stable compiler" source into a temp dir and build it.
  # Note:  we don't want to build the CompilerAdapter.
  mkdir ecj-bootstrap-tmp
  unzip -qq -d ecj-bootstrap-tmp jdtcoresrc/src/ecj.zip
  rm -f ecj-bootstrap-tmp/org/eclipse/jdt/core/JDTCompilerAdapter.java

  # 1a. Build ecj with gcj%gccsuffix -C
  pushd ecj-bootstrap-tmp
  for f in `find -name '*.java' | cut -c 3- | LC_ALL=C sort`; do
      gcj%gccsuffix -I. -Wno-deprecated -C $f
  done
  find -name '*.class' -or -name '*.properties' -or -name '*.rsc' |\
      xargs %{jar} cf ../ecj-bootstrap.jar
  popd
  
  # Delete our modified ecj and restore the backup
  rm -r ecj-bootstrap-tmp
  
  # 1b. Natively-compile it
  gcj%gccsuffix -fPIC -fjni -findirect-dispatch -shared -Wl,-Bsymbolic \
    -o ecj-bootstrap.jar.so ecj-bootstrap.jar

  gcj-dbtool%gccsuffix -n ecj-bootstrap.db 30000
  gcj-dbtool%gccsuffix -a ecj-bootstrap.db ecj-bootstrap.jar{,.so}
  
  # 2a. Build ecj
  export CLASSPATH=ecj-bootstrap.jar:$ORIGCLASSPATH
  export ANT_OPTS="-Dgnu.gcj.precompiled.db.path=`pwd`/ecj-bootstrap.db"
%endif
%{ant} -buildfile jdtcoresrc/compilejdtcorewithjavac.xml

%if %{gcj_support}
  # 2b. Natively-compile ecj
  gcj%gccsuffix -fPIC -fjni -findirect-dispatch -shared -Wl,-Bsymbolic \
    -o jdtcoresrc/ecj.jar.so jdtcoresrc/ecj.jar
   
  gcj-dbtool%gccsuffix -n jdtcoresrc/ecj.db 30000
  gcj-dbtool%gccsuffix -a jdtcoresrc/ecj.db jdtcoresrc/ecj.jar{,.so}

  # Remove our gcj%gccsuffix-built ecj
  rm ecj-bootstrap.db ecj-bootstrap.jar{,.so}

  # To enSURE we're not using any pre-compiled ecj on the build system, set this
  export ANT_OPTS="-Dgnu.gcj.precompiled.db.path=`pwd`/jdtcoresrc/ecj.db"
%endif

# 3. Use this ecj to rebuild itself
export CLASSPATH=`pwd`/jdtcoresrc/ecj.jar:$ORIGCLASSPATH
%{ant} -buildfile jdtcoresrc/compilejdtcore.xml

%if %{gcj_support}
  # Natively-compile it
  gcj%gccsuffix -fPIC -fjni -findirect-dispatch -shared -Wl,-Bsymbolic \
    -o ecj.jar.so ecj.jar
  gcj-dbtool%gccsuffix -n ecj.db 30000
  gcj-dbtool%gccsuffix -a ecj.db ecj.jar{,.so}
  export ANT_OPTS="-Dgnu.gcj.precompiled.db.path=`pwd`/ecj.db"
  
  # Remove old native bits
  rm jdtcoresrc/ecj.db jdtcoresrc/ecj.jar.so
%endif

# Build the rest of Eclipse
export CLASSPATH=`pwd`/ecj.jar:$ORIGCLASSPATH
export JAVA_HOME=%{java_home}
%{ant} \
  -Dnobootstrap=true \
  -DinstallOs=linux -DinstallWs=gtk -DinstallArch=%{eclipse_arch} \
  -Dlibsconfig=true -DjavacSource=1.5 -DjavacTarget=1.5
# -Djava.home=%{_jvmdir}/java-1.5.0-gcj-1.5.0.0/jre

# Build the FileInitializer application
SDK=$(cd eclipse && pwd)
PDEPLUGINVERSION=$(ls $SDK/plugins | grep pde.build | sed 's/org.eclipse.pde.build_//')
pushd equinox-incubator
mkdir -p build
mkdir -p home
homedir=$(cd home && pwd)

# This can go away when package build handles plugins (not just features)
echo "<project default=\"main\"><target name=\"main\"></target></project>" > build/assemble.org.eclipse.equinox.initializer.all.xml
echo "<project default=\"main\"><target name=\"main\"></target></project>" > build/package.org.eclipse.equinox.initializer.all.xml

%{java} -cp $SDK/startup.jar \
      org.eclipse.core.launcher.Main \
     -Duser.home=$homedir                              \
     -application org.eclipse.ant.core.antRunner       \
     -Dtype=plugin                                    \
     -Did=org.eclipse.equinox.initializer                   \
     -DsourceDirectory=$(pwd)                          \
     -DbaseLocation=$SDK \
     -Dbuilder=$SDK/plugins/org.eclipse.pde.build_$PDEPLUGINVERSION/templates/package-build  \
     -f $SDK/plugins/org.eclipse.pde.build_$PDEPLUGINVERSION/scripts/build.xml

pushd build/plugins/org.eclipse.equinox.initializer
%{java} -cp $SDK/startup.jar \
      org.eclipse.core.launcher.Main \
     -Duser.home=$homedir                              \
     -application org.eclipse.ant.core.antRunner       \
     -f build.xml build.update.jar
popd

popd

%install
rm -rf $RPM_BUILD_ROOT

# Get swt version
SWT_MAJ_VER=$(grep maj_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_MIN_VER=$(grep min_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_VERSION=$SWT_MAJ_VER$SWT_MIN_VER

# Some directories we need
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/links
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/features

# Explode the resulting SDK tarball
tar -C $RPM_BUILD_ROOT%{_datadir} -zxf result/linux-gtk-%{eclipse_arch}-sdk.tar.gz

# The FileInitializer app isn't part of the SDK (yet?) but we want it to be
# around for other RPMs
cp equinox-incubator/org.eclipse.equinox.initializer/org.eclipse.equinox.initializer_*.jar \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins

# Set up an extension location and a link file for the arch-specific dir
echo "path:$RPM_BUILD_ROOT%{_libdir}" > $RPM_BUILD_ROOT%{_datadir}/%{name}/links/fragments.link
echo "name=Eclipse Platform" > $RPM_BUILD_ROOT%{_libdir}/%{name}/.eclipseextension
echo "id=org.eclipse.platform" >> $RPM_BUILD_ROOT%{_libdir}/%{name}/.eclipseextension
echo "version=%{eclipse_majmin}.%{eclipse_micro}" >> $RPM_BUILD_ROOT%{_libdir}/%{name}/.eclipseextension

# Install the platform-specific fragments in an arch-specific dir
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/*%{eclipse_arch}* $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

# platform.source has the launcher src zip which is platform-specific
PLATFORMSOURCEVERSION=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep platform.source_ | sed 's/org.eclipse.platform.source_//')
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/org.eclipse.platform.source_$PLATFORMSOURCEVERSION \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

# help.webapp generates web.xml with Apache Jakarta Tomcat JspC. This file is
# generated differently for different archs. FIXME investigate this.
HELPWEBAPPVERSION=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep help.webapp_ | sed 's/org.eclipse.help.webapp_//')
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/org.eclipse.help.webapp_$HELPWEBAPPVERSION \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

# update.core.linux is a fragment
# FIXME: make a patch for upstream to change to swt fragment notation
UPDATECORELINUXVERSION=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep update.core.linux_ | sed 's/org.eclipse.update.core.linux_//')
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/org.eclipse.update.core.linux_$UPDATECORELINUXVERSION \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

# FIXME: icu4j generates res_index.txt differently on different archs - possible libgcj bug.
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/com.ibm.icu_3.4.5.20061213.jar $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/com.ibm.icu.source_3.4.5.20061213 $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

# FIXME: there is a problem with gjdoc generating different HTML on different
# architectures.
PLATFORMDOCISVVERSION=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep platform.doc.isv_ | sed 's/org.eclipse.platform.doc.isv_//')
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/org.eclipse.platform.doc.isv_$PLATFORMDOCISVVERSION \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins
# ppc64 is problematic with these two
JDTDOCISVVERSION=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep jdt.doc.isv_ | sed 's/org.eclipse.jdt.doc.isv_//')
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/org.eclipse.jdt.doc.isv_$JDTDOCISVVERSION \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins
PDEDOCUSERVERSION=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep pde.doc.user_ | sed 's/org.eclipse.pde.doc.user_//')
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/org.eclipse.pde.doc.user_$PDEDOCUSERVERSION \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

# Adding support for ppc64, s390{x} and sparc{64} makes the rcp feature 
# have multilib conflicts
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/features/org.eclipse.rcp_* \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/features

# To ensure that the product is org.eclipse.sdk.ide when eclipse-sdk is
# installed, we must check for its presence at %%post{,un} time.  This does not
# work in the biarch case, though, if it is not in an arch-specific location.
# This results in complaints that the sdk plugin is found twice, but this is
# better than always appearing in the about dialog as the Eclipse Platform with
# the platform plugin version number instead of the actual SDK version number.
# -- overholt, 2006-11-03
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/org.eclipse.sdk_* \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/features/org.eclipse.sdk_* \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/features

# FIXME: investigate why it doesn't work to set this -- configuration data is
# always written to /usr/share/eclipse/configuration, even with
#     -Dosgi.sharedConfiguration.area=$RPM_BUILD_ROOT%{_libdir}/%{name}/configuration
# Note (2006-12-05):  upon looking at this again, we (bkonrath, overholt) don't
# know what we're doing with $libdir_path :)  It requires some investigation.
# 
# Extract .so files
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=90535
pushd $RPM_BUILD_ROOT
datadir_path=$(echo %{_datadir}/%{name} | sed -e 's/^\///')
libdir_path=$(echo %{_libdir}/%{name} | sed -e 's/^\///')
%{java} -Dosgi.sharedConfiguration.area=$libdir_path/configuration \
     -cp $datadir_path/startup.jar \
     org.eclipse.core.launcher.Main \
     -consolelog \
     -application org.eclipse.equinox.initializer.configInitializer \
     -fileInitializer %{SOURCE19}
popd

# Make proper links file
echo "path:/usr/lib" > $RPM_BUILD_ROOT%{_datadir}/%{name}/links/fragments.link
echo "path:/usr/lib64" > $RPM_BUILD_ROOT%{_datadir}/%{name}/links/fragments64.link

# Install config.ini to an arch dependent location and remove the unnecessary
# configuration data
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/configuration $RPM_BUILD_ROOT%{_libdir}/%{name}
rm -r $RPM_BUILD_ROOT%{_libdir}/%{name}/configuration/org.eclipse.update
rm -r $RPM_BUILD_ROOT%{_libdir}/%{name}/configuration/org.eclipse.core.runtime

# Set config.ini for the platform; no benefit to having it be sdk
sed --in-place "s/eclipse.product=org.eclipse.sdk.ide/eclipse.product=org.eclipse.platform.ide/" \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/configuration/config.ini

# Install the Eclipse binary
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
%if 0
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/eclipse $RPM_BUILD_ROOT%{_bindir}/%{name}
%else
%{__perl} -pe \
  's|/usr/lib/eclipse/|%{_libdir}/%{name}/|g ;
   s|/etc/|%{_sysconfdir}/|g ;
   s|/usr/bin/|%{_bindir}/|g ;
   s|/usr/lib/|%{_libdir}/|g ;
   s|\@FIREFOX_DIR\@|%{firefox_dir}|g' \
  %{SOURCE1} > $RPM_BUILD_ROOT%{_bindir}/eclipse
chmod a+x $RPM_BUILD_ROOT%{_bindir}/eclipse
%endif

# Default config
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
%{__perl} -pe 's|/usr/lib/eclipse/|%{_datadir}/%{name}/|g' \
  %{SOURCE6} > $RPM_BUILD_ROOT%{_sysconfdir}/eclipse.conf

# Ensure the shared libraries have the correct permissions
pushd $RPM_BUILD_ROOT%{_libdir}/%{name} 
for lib in `find configuration -name \*.so`; do
   chmod 755 $lib
done

%if 0
# http://qa.mandriva.com/show_bug.cgi?id=21682
%{__rm} -r %{buildroot}%{_libdir}/%{name}/configuration/org.eclipse.osgi
%endif

# Create file listings for the extracted shared libraries
echo -n "" > %{_builddir}/%{buildsubdir}/%{libname}-gtk2.install;
echo -n "" > %{_builddir}/%{buildsubdir}/%{name}-platform.install;
for id in `ls configuration/org.eclipse.osgi/bundles`; do
  if [ "Xconfiguration" = $(echo X`find configuration/org.eclipse.osgi/bundles/$id -name libswt\*.so` | sed "s:/.*::") ]; then
    echo "%{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles/$id" > %{_builddir}/%{buildsubdir}/%{libname}-gtk2.install;
  else
    echo "%{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles/$id" >> %{_builddir}/%{buildsubdir}/%{name}-platform.install;
  fi
done 
popd

# Install symlinks to the SWT JNI shared libraries in /usr/lib/eclipse
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
for lib in $(find configuration -name libswt\*.so); do  
  ln -s %{_libdir}/%{name}/$lib `basename $lib`
done
popd

# (anssi) Other software depending on swt-gtk-3.2.jar load these too, so
# put them back in %{_libdir} too.
pushd $RPM_BUILD_ROOT%{_libdir}
for lib in $(find %{name}/configuration -name libswt\*.so); do
  ln -s %{_libdir}/$lib `basename $lib`
done
popd

# (anssi) Other software depends on swt-gtk-3.2.jar too, so put it in
# jnidir which is for arch-dependent jars.
# Install the SWT jar symlinks in jnidir
SWTJARVERSION=$(grep v$SWT_VERSION plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}/build.xml | sed "s:.*<.*\"\(.*\)\"/>:\1:")
install -d -m755 $RPM_BUILD_ROOT%{_jnidir}
pushd $RPM_BUILD_ROOT%{_jnidir}
ln -s %{_libdir}/%{name}/plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}_$SWTJARVERSION.jar swt-gtk-%{eclipse_majmin}.%{eclipse_micro}.jar
ln -s swt-gtk-%{eclipse_majmin}.%{eclipse_micro}.jar swt-gtk-%{eclipse_majmin}.jar
popd

# Install the eclipse-ecj.jar symlink for java-1.4.2-gcj-compat's "javac"
JDTCORESUFFIX=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep jdt.core_ | sed "s/org.eclipse.jdt.core_//")
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
ln -s %{_datadir}/%{name}/plugins/org.eclipse.jdt.core_$JDTCORESUFFIX $RPM_BUILD_ROOT%{_javadir}/eclipse-ecj.jar
ln -s %{_javadir}/eclipse-ecj.jar $RPM_BUILD_ROOT%{_javadir}/jdtcore.jar
ln -s %{_javadir}/eclipse-ecj.jar $RPM_BUILD_ROOT%{_javadir}/ecj.jar

# FIXME: get rid of this by putting logic in package build to know what version
#        of pde.build it's using
# Install a versionless pde.build
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/
ln -s org.eclipse.pde.build_* org.eclipse.pde.build
popd

# Icons
PLATFORMSUFFIX=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep eclipse.platform_ | sed "s/org.eclipse.platform_//")
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
ln -s %{_datadir}/%{name}/plugins/org.eclipse.platform_$PLATFORMSUFFIX/eclipse48.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
ln -s %{_datadir}/%{name}/plugins/org.eclipse.platform_$PLATFORMSUFFIX/eclipse32.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
ln -s ../../../../%{name}/plugins/org.eclipse.platform_$PLATFORMSUFFIX/eclipse.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pixmaps
ln -s %{_datadir}/icons/hicolor/48x48/apps/%{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/pixmaps
%ifarch %{ix86} x86_64
# Remove unused icon.xpm
# This should be fixed in 3.3.
# see https://bugs.eclipse.org/bugs/show_bug.cgi?id=86848
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/icon.xpm
%endif

# Install the efj wrapper script 
install -p -D -m0755 %{SOURCE17} $RPM_BUILD_ROOT%{_bindir}/efj
sed --in-place "s:startup.jar:%{_datadir}/%{name}/startup.jar:" \
  $RPM_BUILD_ROOT%{_bindir}/efj 

# Install the ecj wrapper script
install -p -D -m0755 %{SOURCE18} $RPM_BUILD_ROOT%{_bindir}/ecj
sed --in-place -e "s:@JAVADIR@:%{_javadir}:;" -e "s:@gccsuffix@:%{gccsuffix}:;" $RPM_BUILD_ROOT%{_bindir}/ecj 

# A sanity check.
desktop-file-validate %{SOURCE2}

# freedesktop.org menu entry
install -p -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

SDKPLUGINVERSION=$(ls $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins | grep eclipse.sdk_ | sed "s/org.eclipse.sdk_//")
# Put Fedora Core version into about.mappings of org.eclipse.sdk and
# org.eclipse.platform to show it in # Eclipse about dialog.  (courtesy Debian
# Eclipse packagers)
# FIXME use the third id
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/org.eclipse.sdk_$SDKPLUGINVERSION
OS_VERSION=$(cat /etc/*-release | head -n 1)
sed -e "s/\(0=.*\)/\1 ($OS_VERSION)/" < about.mappings > about.mappings.tmp
mv about.mappings.tmp about.mappings
popd
PLATFORMPLUGINVERSION=$(ls $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins | grep eclipse.platform_ | sed "s/org.eclipse.platform_//")
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/org.eclipse.platform_$PLATFORMPLUGINVERSION
sed -e "s/\(0=.*\)/\1 ($OS_VERSION)/" < about.mappings > about.mappings.tmp
mv about.mappings.tmp about.mappings
popd

# Create a script that can be used to make a symlink tree of the
# eclipse platform.
cp %{SOURCE16} copy-platform
(
  cd $RPM_BUILD_ROOT%{_datadir}/%{name}
  ls -d * | egrep -v '^(plugins|features|links|about_files)$'
  ls -d plugins/* features/* links/*
) |
sed -e's/^\(.*\)$/\1 \1/' -e's,^,ln -s $eclipse/,' >> copy-platform

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/buildscripts
cp copy-platform $RPM_BUILD_ROOT%{_datadir}/%{name}/buildscripts

pushd $RPM_BUILD_ROOT%{_datadir}/%{name}
## BEGIN ANT ##
rm plugins/org.apache.ant_*/lib/ant-antlr.jar
rm plugins/org.apache.ant_*/lib/ant-apache-bcel.jar
rm plugins/org.apache.ant_*/lib/ant-apache-bsf.jar
rm plugins/org.apache.ant_*/lib/ant-apache-log4j.jar
rm plugins/org.apache.ant_*/lib/ant-apache-oro.jar
rm plugins/org.apache.ant_*/lib/ant-apache-regexp.jar
rm plugins/org.apache.ant_*/lib/ant-apache-resolver.jar
rm plugins/org.apache.ant_*/lib/ant-commons-logging.jar
rm plugins/org.apache.ant_*/lib/ant-commons-net.jar
#rm plugins/org.apache.ant_*/lib/ant-icontract.jar
#rm plugins/org.apache.ant_*/lib/ant-jai.jar
rm plugins/org.apache.ant_*/lib/ant.jar
rm plugins/org.apache.ant_*/lib/ant-javamail.jar
rm plugins/org.apache.ant_*/lib/ant-jdepend.jar
rm plugins/org.apache.ant_*/lib/ant-jmf.jar
rm plugins/org.apache.ant_*/lib/ant-jsch.jar
rm plugins/org.apache.ant_*/lib/ant-junit.jar
rm plugins/org.apache.ant_*/lib/ant-launcher.jar
#rm plugins/org.apache.ant_*/lib/ant-netrexx.jar
rm plugins/org.apache.ant_*/lib/ant-nodeps.jar
#rm plugins/org.apache.ant_*/lib/ant-starteam.jar
#rm plugins/org.apache.ant_*/lib/ant-stylebook.jar
rm plugins/org.apache.ant_*/lib/ant-swing.jar
rm plugins/org.apache.ant_*/lib/ant-trax.jar
#rm plugins/org.apache.ant_*/lib/ant-vaj.jar
#rm plugins/org.apache.ant_*/lib/ant-weblogic.jar
#rm plugins/org.apache.ant_*/lib/ant-xalan1.jar
#rm plugins/org.apache.ant_*/lib/ant-xslp.jar
# FIXME use build-jar-repository
ln -s %{_javadir}/ant/ant-antlr.jar plugins/org.apache.ant_1.6.5/lib/ant-antlr.jar
ln -s %{_javadir}/ant/ant-apache-bcel.jar plugins/org.apache.ant_1.6.5/lib/ant-apache-bcel.jar
ln -s %{_javadir}/ant/ant-apache-bsf.jar plugins/org.apache.ant_1.6.5/lib/ant-apache-bsf.jar
ln -s %{_javadir}/ant/ant-apache-log4j.jar plugins/org.apache.ant_1.6.5/lib/ant-apache-log4j.jar
ln -s %{_javadir}/ant/ant-apache-oro.jar plugins/org.apache.ant_1.6.5/lib/ant-apache-oro.jar
ln -s %{_javadir}/ant/ant-apache-regexp.jar plugins/org.apache.ant_1.6.5/lib/ant-apache-regexp.jar
ln -s %{_javadir}/ant/ant-apache-resolver.jar plugins/org.apache.ant_1.6.5/lib/ant-apache-resolver.jar
ln -s %{_javadir}/ant/ant-commons-logging.jar plugins/org.apache.ant_1.6.5/lib/ant-commons-logging.jar
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=180642
# the symlinks that are commented out are not currently shipped on Fedora
#ln -s %{_javadir}/ant/ant-commons-net.jar plugins/org.apache.ant_1.6.5/lib/ant-commons-net.jar
#ln -s %{_javadir}/ant/ant-icontract.jar plugins/org.apache.ant_1.6.5/lib/ant-icontract.jar
#ln -s %{_javadir}/ant/ant-jai.jar plugins/org.apache.ant_1.6.5/lib/ant-jai.jar
ln -s %{_javadir}/ant.jar plugins/org.apache.ant_1.6.5/lib/ant.jar
ln -s %{_javadir}/ant/ant-javamail.jar plugins/org.apache.ant_1.6.5/lib/ant-javamail.jar
ln -s %{_javadir}/ant/ant-jdepend.jar plugins/org.apache.ant_1.6.5/lib/ant-jdepend.jar
#ln -s %{_javadir}/ant/ant-jmf.jar plugins/org.apache.ant_1.6.5/lib/ant-jmf.jar
ln -s %{_javadir}/ant/ant-jsch.jar plugins/org.apache.ant_1.6.5/lib/ant-jsch.jar
ln -s %{_javadir}/ant/ant-junit.jar plugins/org.apache.ant_1.6.5/lib/ant-junit.jar
ln -s %{_javadir}/ant-launcher.jar plugins/org.apache.ant_1.6.5/lib/ant-launcher.jar
#ln -s %{_javadir}/ant/ant-netrexx.jar plugins/org.apache.ant_1.6.5/lib/ant-netrexx.jar
ln -s %{_javadir}/ant/ant-nodeps.jar plugins/org.apache.ant_1.6.5/lib/ant-nodeps.jar
#ln -s %{_javadir}/ant/ant-starteam.jar plugins/org.apache.ant_1.6.5/lib/ant-starteam.jar
#ln -s %{_javadir}/ant/ant-stylebook.jar plugins/org.apache.ant_1.6.5/lib/ant-stylebook.jar
ln -s %{_javadir}/ant/ant-swing.jar plugins/org.apache.ant_1.6.5/lib/ant-swing.jar
ln -s %{_javadir}/ant/ant-trax.jar plugins/org.apache.ant_1.6.5/lib/ant-trax.jar
#ln -s %{_javadir}/ant/ant-vaj.jar plugins/org.apache.ant_1.6.5/lib/ant-vaj.jar
#ln -s %{_javadir}/ant/ant-weblogic.jar plugins/org.apache.ant_1.6.5/lib/ant-weblogic.jar
#ln -s %{_javadir}/ant/ant-xalan1.jar plugins/org.apache.ant_1.6.5/lib/ant-xalan1.jar
#ln -s %{_javadir}/ant/ant-xslp.jar plugins/org.apache.ant_1.6.5/lib/ant-xslp.jar
## END ANT ##

## BEGIN LUCENE ##
LUCENEPLUGINVERSION=$(ls plugins | grep lucene | sed 's/org.apache.lucene_//')
rm plugins/org.apache.lucene_$LUCENEPLUGINVERSION/lucene-1.4.3.jar
ln -s %{_javadir}/lucene.jar \
  plugins/org.apache.lucene_$LUCENEPLUGINVERSION/lucene-1.4.3.jar
# org.eclipse.platform.source is in the arch-specific location
## END LUCENE ##
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
PLATFORMSOURCEVERSION=$(ls plugins | grep platform.source_ | sed 's/org.eclipse.platform.source_//')
rm plugins/org.eclipse.platform.source_$PLATFORMSOURCEVERSION/src/org.apache.lucene_$LUCENEPLUGINVERSION/lucene-1.4.3-src.zip
ln -s %{_datadir}/lucene/lucene-src.zip \
  plugins/org.eclipse.platform.source_$PLATFORMSOURCEVERSION/src/org.apache.lucene_$LUCENEPLUGINVERSION/lucene-1.4.3-src.zip
popd
# FIXME: rm and ln lucene-related files
rm plugins/org.apache.lucene_*/lucene-1.4.3.jar
rm plugins/org.apache.lucene_*/parser.jar
# FIXME
ln -s %{_javadir}/lucene.jar plugins/org.apache.lucene_1.4.103.v20060601/lucene-1.4.3.jar
ln -s %{_datadir}/lucene/lucene-demos.jar plugins/org.apache.lucene_1.4.103.v20060601/parser.jar

## BEGIN TOMCAT ##
TOMCATPLUGINVERSION=$(ls plugins | grep tomcat | sed 's/org.eclipse.tomcat_//')
mkdir -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib
ln -s %{tomcatsharedir}/bin/bootstrap.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/bootstrap.jar
ln -s %{tomcatlibdir}/server/lib/catalina.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/catalina.jar
ln -s %{tomcatlibdir}/server/lib/catalina-optional.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/catalina-optional.jar
ln -s %{_javadir}/jasper5-compiler.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/jasper-compiler.jar
ln -s %{_javadir}/jasper5-runtime.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/jasper-runtime.jar
ln -s %{_javadir}/mx4j/mx4j.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/mx4j.jar
ln -s %{_javadir}/mx4j/mx4j-impl.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/mx4j-impl.jar
ln -s %{_javadir}/mx4j/mx4j-jmx.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/mx4j-jmx.jar
ln -s %{tomcatlibdir}/common/lib/naming-factory.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/naming-factory.jar
ln -s %{tomcatlibdir}/common/lib/naming-resources.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/naming-resources.jar
ln -s %{tomcatlibdir}/server/lib/servlets-default.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/servlets-default.jar
ln -s %{tomcatlibdir}/server/lib/servlets-invoker.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/servlets-invoker.jar
ln -s %{tomcatlibdir}/server/lib/tomcat-coyote.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/tomcat-coyote.jar
ln -s %{tomcatlibdir}/server/lib/tomcat-http.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/tomcat-http.jar
ln -s %{tomcatlibdir}/server/lib/tomcat-util.jar plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib/tomcat-util.jar
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-beanutils
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-collections
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-dbcp
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-digester
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-digester-rss
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-el
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-fileupload
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-launcher
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-logging-api
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-modeler
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib commons-pool
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib jspapi
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib regexp
build-jar-repository -s -p plugins/org.eclipse.tomcat_$TOMCATPLUGINVERSION/lib servletapi5
## END TOMCAT ##

build-jar-repository -s -p plugins/org.junit_* junit

junit4dirname=$(dirname plugins/org.junit4_*/junit-4.1.jar)
rm plugins/org.junit4_*/junit-4.1.jar
ln -s %{_javadir}/junit4.jar $junit4dirname/junit-4.1.jar

%if 0
# Ensure that the zip files are the same across all builds.
# This is needed to make these package multilib compatible.
# FIXME: this needs to be re-written as a separate program
# warning: big hack!
mkdir -p ${RPM_BUILD_ROOT}/tmp
for zip in `find ${RPM_BUILD_ROOT}%{_datadir}/%{name} -type f -name \*.zip -o -type f -name \*.jar`; do
  # unpack every zip, set the date of the files and directories and repack the zip
  ZIPNAME=`basename $zip`
  TMPDIR=`mktemp -d -p ${RPM_BUILD_ROOT}/tmp $ZIPNAME.tmpdir.XXXXXXXXXX` 
  ZIPDIR=`mktemp -d -p ${RPM_BUILD_ROOT}/tmp $ZIPNAME.zipdir.XXXXXXXXXX`        
  
  pushd $TMPDIR 
  unzip -qq -o $zip
  rm -f $zip    

  # check if there are jars or zips inside the zip or jar
  zipsinside=`find $TMPDIR -type f -name \*.zip -o -name \*.jar`
  if [ -n "$zipsinside" ]; then
     for zip2 in $zipsinside; do
       # unpack every zip, set the date of the files and directories and repack the zip
       ZIPNAME2=`basename $zip2`
       TMPDIR2=`mktemp -d -p ${RPM_BUILD_ROOT}/tmp $ZIPNAME2.tmpdir.XXXXXXXXXX`
       ZIPDIR2=`mktemp -d -p ${RPM_BUILD_ROOT}/tmp $ZIPNAME2.zipdir.XXXXXXXXXX`

       pushd $TMPDIR2
       unzip -qq -o $zip2
       rm -f $zip2

       # create the directories first
       for d in `find -type d | LC_ALL=C sort`; do
         mkdir -p $ZIPDIR2/$d
       done
       # move the contents over to the a new directory in order and set the times. 
       for f in `find -type f | LC_ALL=C sort`; do
         cp $f $ZIPDIR2/$f
         touch --date="1970-01-01 UTC" $ZIPDIR2/$f
       done
       popd

       # Set the times of the directories.
       touch --date="1970-01-01 UTC" `find $ZIPDIR2 -type d`

       # make the new zip
       pushd $ZIPDIR2
       find -type f -print | LC_ALL=C sort | /usr/bin/zip -q -X -9 $zip2 -@
       popd

       # Cleanup.
       rm -rf $TMPDIR2
       rm -rf $ZIPDIR2
     done
  fi 
  
  # now on to the original zip or jar.
  # create the directories first
  for d in `find -type d | LC_ALL=C sort`; do
    mkdir -p $ZIPDIR/$d
  done 
  # move the contents over to the a new directory in order and set the times. 
  for f in `find -type f | LC_ALL=C sort`; do 
    cp $f $ZIPDIR/$f
    touch --date="1970-01-01 UTC" $ZIPDIR/$f
  done
  popd

  # Set the times of the directories.
  touch --date="1970-01-01 UTC" `find $ZIPDIR -type d`

  # make the new zip
  pushd $ZIPDIR
  find -type f -print | LC_ALL=C sort | /usr/bin/zip -q -X -9 $zip -@
  popd

  # Cleanup.
  rm -rf $TMPDIR
  rm -rf $ZIPDIR
done
rm -rf ${RPM_BUILD_ROOT}/tmp
%endif

pushd plugins/org.apache.ant_*/bin
for i in ant antRun antRun.pl complete-ant-cmd.pl runant.pl runant.py; do
  test -e $i && %{__rm} $i && %{__ln_s} %{_bindir}/$i $i || exit 1
done
popd

%if 0
# remove this python script so that it is not aot compiled, thus avoiding a
# multilib conflict
ANTPLUGINVERSION=$(ls plugins | grep org.apache.ant_ | sed 's/org.apache.ant_//')
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/org.apache.ant_$ANTPLUGINVERSION/bin/runant.py
%endif

%if %{gcj_support}
# exclude org.eclipse.ui.ide to work around
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=175547
UIIDEPLUGINVERSION=$(ls plugins | grep ui.ide_ | sed 's/org.eclipse.ui.ide_//')
%ifnarch ia64
%{_bindir}/aot-compile-rpm --exclude %{_datadir}/%{name}/plugins/org.eclipse.ui.ide_$UIIDEPLUGINVERSION
%else
OSGIPLUGINVERSION=$(ls plugins | grep osgi_ | sed 's/org.eclipse.osgi_//')
%{_bindir}/aot-compile-rpm --exclude %{_datadir}/%{name}/plugins/org.eclipse.ui.ide_$UIIDEPLUGINVERSION \
                --exclude %{_datadir}/%{name}/plugins/com.jcraft.jsch_0.1.28.jar \
                --exclude %{_datadir}/%{name}/plugins/org.eclipse.osgi_$OSGIPLUGINVERSION
%endif
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post platform
%if %{gcj_support}
%{update_gcjdb}
%endif
%{update_desktop_database}
%update_icon_cache hicolor

%postun platform
%if %{gcj_support}
%{clean_gcjdb}
%endif
%{update_desktop_database}
%update_icon_cache hicolor

%post sdk
%if %{gcj_support}
%{update_gcjdb}
%endif
if [ -f %{_libdir}/%{name}/configuration/config.ini ]; then
  sed --in-place "s/[#]*eclipse.product=.*/eclipse.product=org.eclipse.sdk.ide/" \
    %{_libdir}/%{name}/configuration/config.ini
fi

%postun sdk
%if %{gcj_support}
%{clean_gcjdb}
%endif
# Only set the product back to platform.ide if the sdk is actually removed for
# this arch.  This SDKDIR check is to deal with the ordering of new %%post
# before old %%postun
if [ -d %{_libdir}/%{name}/features ]; then
  SDKDIR=$(ls %{_libdir}/%{name}/features | grep "org\.eclipse\.sdk_")
else
  SDKDIR=""
fi
if [ -z "$SDKDIR" -a -f %{_libdir}/%{name}/configuration/config.ini ]; then
  sed --in-place "s/[#]*eclipse.product=.*/eclipse.product=org.eclipse.platform.ide/" \
    %{_libdir}/%{name}/configuration/config.ini
fi

%if %{gcj_support}
%post ecj
%{update_gcjdb}

%postun ecj
%{clean_gcjdb}

%post -n %{libname}-gtk2
%{update_gcjdb}

%postun -n %{libname}-gtk2
%{clean_gcjdb}

%post rcp
%{update_gcjdb}

%postun rcp
%{clean_gcjdb}

%post rcp-sdk
%{update_gcjdb}

%postun rcp-sdk
%{clean_gcjdb}

%post platform-sdk
%{update_gcjdb}

%postun platform-sdk
%{clean_gcjdb}

%post jdt
%{update_gcjdb}

%postun jdt
%{clean_gcjdb}

%post jdt-sdk
%{update_gcjdb}

%postun jdt-sdk
%{clean_gcjdb}

%post pde
%{update_gcjdb}

%postun pde
%{clean_gcjdb}

%post pde-runtime
%{update_gcjdb}

%postun pde-runtime
%{clean_gcjdb}

%post pde-sdk
%{update_gcjdb}

%postun pde-sdk
%{clean_gcjdb}
%endif

%files ecj
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/org.eclipse.jdt.core_*
%{_javadir}/ecj.jar
%{_javadir}/eclipse-ecj.jar
%{_javadir}/jdtcore.jar
%{_bindir}/ecj
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/org.eclipse.jdt.core_*
%endif

%files -n %{libname}-gtk2 -f %{libname}-gtk2.install
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_libdir}/libswt-*.so
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/libswt-*.so
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/configuration
%if 1
%dir %{_libdir}/%{name}/configuration/org.eclipse.osgi
%dir %{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles
%endif
%{_datadir}/%{name}/plugins/org.eclipse.swt_*
%{_libdir}/%{name}/plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}_*
# FIXME: do we need to build?
#%{_libdir}/%{name}/libcairo-swt.so
%{_jnidir}/swt-gtk*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/org.eclipse.swt.gtk.linux.%{eclipse_arch}_*
%endif

%files rcp
%defattr(-,root,root)
%dir %{_datadir}/%{name}/features
%if 1
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.bundledata*
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.lazy*
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.manager
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.state*
%endif
%{_libdir}/%{name}/configuration/config.ini
%{_libdir}/%{name}/.eclipseextension
%if 0
%{_datadir}/%{name}/configuration/org.eclipse.core.runtime
%{_datadir}/%{name}/configuration/org.eclipse.update
%endif
%{_datadir}/%{name}/.eclipseproduct
%{_datadir}/%{name}/notice.html
%{_datadir}/%{name}/epl-v10.html
%{_datadir}/%{name}/links
%ifarch %{ix86} x86_64
%{_datadir}/%{name}/about.html
%endif
%{_datadir}/%{name}/startup.jar
%ifarch x86_64
%{_datadir}/%{name}/about_files
%endif
%{_datadir}/%{name}/readme
%{_libdir}/%{name}/features/org.eclipse.rcp_*
%{_datadir}/%{name}/plugins/org.eclipse.update.configurator_*
%{_datadir}/%{name}/plugins/org.eclipse.osgi_*
%{_datadir}/%{name}/plugins/org.eclipse.equinox.registry_*
%{_libdir}/%{name}/plugins/com.ibm.icu_*
%{_datadir}/%{name}/plugins/org.eclipse.jface_*
%{_datadir}/%{name}/plugins/org.eclipse.jface.databinding_*
%{_datadir}/%{name}/plugins/org.eclipse.core.commands_*
%{_datadir}/%{name}/plugins/org.eclipse.core.runtime.compatibility.auth_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.workbench_*
%{_datadir}/%{name}/plugins/org.eclipse.core.jobs_*
%{_datadir}/%{name}/plugins/org.eclipse.ui_*
%{_datadir}/%{name}/plugins/org.eclipse.core.runtime_*
%{_datadir}/%{name}/plugins/org.eclipse.equinox.preferences_*
%{_datadir}/%{name}/plugins/org.eclipse.core.expressions_*
%{_datadir}/%{name}/plugins/org.eclipse.equinox.common_*
%{_datadir}/%{name}/plugins/org.eclipse.help_*
%{_datadir}/%{name}/plugins/org.eclipse.core.contenttype_*
%{_datadir}/%{name}/plugins/org.eclipse.rcp_*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.update.configurator_*
%ifnarch ia64
%{_libdir}/gcj/%{name}/org.eclipse.osgi_*
%endif
%{_libdir}/gcj/%{name}/org.eclipse.equinox.registry_*
%{_libdir}/gcj/%{name}/com.ibm.icu_*
%{_libdir}/gcj/%{name}/org.eclipse.jface_*
%{_libdir}/gcj/%{name}/org.eclipse.jface.databinding_*
%{_libdir}/gcj/%{name}/org.eclipse.core.commands_*
%{_libdir}/gcj/%{name}/org.eclipse.core.runtime.compatibility.auth_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.workbench_*
%{_libdir}/gcj/%{name}/org.eclipse.core.jobs_*
%{_libdir}/gcj/%{name}/org.eclipse.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.core.runtime_*
%{_libdir}/gcj/%{name}/org.eclipse.equinox.preferences_*
%{_libdir}/gcj/%{name}/org.eclipse.core.expressions_*
%{_libdir}/gcj/%{name}/org.eclipse.equinox.common_*
%{_libdir}/gcj/%{name}/org.eclipse.help_*
%{_libdir}/gcj/%{name}/org.eclipse.core.contenttype_*
%{_libdir}/gcj/%{name}/startup.jar*
%endif

%files rcp-sdk
%defattr(-,root,root)
%{_datadir}/%{name}/features/org.eclipse.rcp.source_*
%{_libdir}/%{name}/plugins/org.eclipse.rcp.source.linux.gtk.%{eclipse_arch}*
%{_datadir}/%{name}/plugins/org.eclipse.rcp.source_*
%{_libdir}/%{name}/plugins/com.ibm.icu.source_*

%files platform -f %{name}-platform.install
%defattr(-,root,root)
%{_datadir}/%{name}/eclipse
%attr(0755,root,root) %{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/eclipse.conf
%{_datadir}/%{name}/eclipse.ini
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/*/*/apps/*
%{_datadir}/%{name}/features/org.eclipse.platform_*
%{_datadir}/%{name}/plugins/org.eclipse.equinox.initializer_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.navigator.resources_*
%{_datadir}/%{name}/plugins/org.eclipse.team.cvs.ui_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.navigator_*
%{_datadir}/%{name}/plugins/org.eclipse.team.cvs.core_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.workbench.compatibility_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.forms_*
%{_datadir}/%{name}/plugins/org.eclipse.ltk.core.refactoring_*
%{_datadir}/%{name}/plugins/org.eclipse.debug.ui_*
%{_datadir}/%{name}/plugins/org.eclipse.core.resources_*
%{_datadir}/%{name}/plugins/org.eclipse.jface.text_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.intro_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.ide_*
%{_datadir}/%{name}/plugins/com.jcraft.jsch_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.cheatsheets_*
%{_datadir}/%{name}/plugins/org.eclipse.ant.core_*
%{_datadir}/%{name}/plugins/org.eclipse.help.appserver_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.browser_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.presentations.r21_*
%{_datadir}/%{name}/plugins/org.eclipse.team.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.update.core.linux_*
%ifarch %{ix86} x86_64
%{_libdir}/%{name}/plugins/org.eclipse.core.filesystem.linux.%{eclipse_arch}_*
%endif
%{_datadir}/%{name}/plugins/org.eclipse.core.variables_*
%{_datadir}/%{name}/plugins/org.eclipse.help.base_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.views.properties.tabbed_*
%{_datadir}/%{name}/plugins/org.eclipse.compare_*
%{_datadir}/%{name}/plugins/org.eclipse.team.core_*
%{_datadir}/%{name}/plugins/org.eclipse.osgi.util_*
%{_datadir}/%{name}/plugins/org.eclipse.osgi.services_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.console_*
%{_datadir}/%{name}/plugins/org.eclipse.platform_*
%{_datadir}/%{name}/plugins/org.eclipse.update.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.help.webapp_*
%{_datadir}/%{name}/plugins/org.eclipse.core.runtime.compatibility_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.views_*
%{_datadir}/%{name}/plugins/org.eclipse.update.core_*
%{_datadir}/%{name}/plugins/org.eclipse.core.resources.compatibility_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.intro.universal_*
%{_datadir}/%{name}/plugins/org.eclipse.core.boot_*
%{_datadir}/%{name}/plugins/org.apache.ant_*
%{_datadir}/%{name}/plugins/org.eclipse.team.cvs.ssh2_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.externaltools_*
%{_datadir}/%{name}/plugins/org.eclipse.team.cvs.ssh_*
%{_datadir}/%{name}/plugins/org.apache.lucene_*
%{_datadir}/%{name}/plugins/org.eclipse.update.scheduler_*
%{_datadir}/%{name}/plugins/org.eclipse.debug.core_*
%{_datadir}/%{name}/plugins/org.eclipse.help.ui_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.editors_*
%{_datadir}/%{name}/plugins/org.eclipse.core.filesystem_*
%{_datadir}/%{name}/plugins/org.eclipse.tomcat_*
%{_datadir}/%{name}/plugins/org.eclipse.core.filebuffers_*
%{_datadir}/%{name}/plugins/org.eclipse.core.runtime.compatibility.registry_*
%{_datadir}/%{name}/plugins/org.eclipse.platform.doc.user_*
%{_datadir}/%{name}/plugins/org.eclipse.ltk.ui.refactoring_*
%{_datadir}/%{name}/plugins/org.eclipse.ui.workbench.texteditor_*
%{_datadir}/%{name}/plugins/org.eclipse.text_*
%{_datadir}/%{name}/plugins/org.eclipse.search_*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.equinox.initializer_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.navigator.resources_*
%{_libdir}/gcj/%{name}/org.eclipse.team.cvs.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.navigator_*
%{_libdir}/gcj/%{name}/org.eclipse.team.cvs.core_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.forms_*
%{_libdir}/gcj/%{name}/org.eclipse.ltk.core.refactoring_*
%{_libdir}/gcj/%{name}/org.eclipse.debug.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.core.resources_*
%{_libdir}/gcj/%{name}/org.eclipse.jface.text_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.intro_*
#%{_libdir}/gcj/%{name}/org.eclipse.ui.ide_*
%ifnarch ia64
%{_libdir}/gcj/%{name}/com.jcraft.jsch_*
%endif
%{_libdir}/gcj/%{name}/org.eclipse.ui.cheatsheets_*
%{_libdir}/gcj/%{name}/org.eclipse.ant.core_*
%{_libdir}/gcj/%{name}/org.eclipse.help.appserver_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.browser_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.presentations.r21_*
%{_libdir}/gcj/%{name}/org.eclipse.team.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.core.variables_*
%{_libdir}/gcj/%{name}/org.eclipse.help.base_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.views.properties.tabbed_*
%{_libdir}/gcj/%{name}/org.eclipse.compare_*
%{_libdir}/gcj/%{name}/org.eclipse.team.core_*
%{_libdir}/gcj/%{name}/org.eclipse.osgi.util_*
%{_libdir}/gcj/%{name}/org.eclipse.osgi.services_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.console_*
%{_libdir}/gcj/%{name}/org.eclipse.update.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.core.runtime.compatibility_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.views_*
%{_libdir}/gcj/%{name}/org.eclipse.update.core_*
%{_libdir}/gcj/%{name}/org.eclipse.core.resources.compatibility_*
%{_libdir}/gcj/%{name}/org.eclipse.team.cvs.ssh2_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.externaltools_*
%{_libdir}/gcj/%{name}/org.eclipse.team.cvs.ssh_*
%{_libdir}/gcj/%{name}/org.eclipse.update.scheduler_*
%{_libdir}/gcj/%{name}/org.eclipse.debug.core_*
%{_libdir}/gcj/%{name}/org.eclipse.help.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.editors_*
%{_libdir}/gcj/%{name}/org.eclipse.core.filesystem_*
%{_libdir}/gcj/%{name}/org.eclipse.core.filebuffers_*
%{_libdir}/gcj/%{name}/org.eclipse.ltk.ui.refactoring_*
%{_libdir}/gcj/%{name}/org.eclipse.ui.workbench.texteditor_*
%{_libdir}/gcj/%{name}/org.eclipse.text_*
%{_libdir}/gcj/%{name}/org.eclipse.search_*
%{_libdir}/gcj/%{name}/universal.jar*
%{_libdir}/gcj/%{name}/webapp.jar*
%{_libdir}/gcj/%{name}/tomcatwrapper.jar*
%{_libdir}/gcj/%{name}/compatibility.jar*
%{_libdir}/gcj/%{name}/platform.jar*
%{_libdir}/gcj/%{name}/runtime_registry_compatibility.jar*
%{_libdir}/gcj/%{name}/servlets.jar*
# FIXME:  we need to symlink these
%if 0
%{_libdir}/gcj/%{name}/ant-apache-bsf.jar*
%endif
%{_libdir}/gcj/%{name}/jsp.jar*
%if 0
%{_libdir}/gcj/%{name}/parser.jar*
%endif
%endif

%files platform-sdk
%defattr(-,root,root)
%{_datadir}/%{name}/features/org.eclipse.platform.source_*
%{_libdir}/%{name}/plugins/org.eclipse.platform.source.linux.gtk.%{eclipse_arch}_*
%{_libdir}/%{name}/plugins/org.eclipse.platform.doc.isv_*
%{_libdir}/%{name}/plugins/org.eclipse.platform.source_*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.platform.doc.isv_*
%endif

%files jdt
%defattr(-,root,root)
%{_bindir}/efj
%{_datadir}/%{name}/features/org.eclipse.jdt_*
%{_datadir}/%{name}/plugins/org.eclipse.ant.ui_*
%{_datadir}/%{name}/plugins/org.junit_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.junit_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.doc.user_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.apt.core_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.ui_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.debug_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.junit4.runtime_*
%{_datadir}/%{name}/plugins/org.junit4_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.launching_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.core.manipulation_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.apt.ui_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.junit.runtime_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.debug.ui_*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/junit-4.1.jar*
%{_libdir}/gcj/%{name}/org.eclipse.ant.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.apt.core_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.junit4.runtime_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.launching_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.core.manipulation_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.apt.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.jdt.debug.ui_*
%{_libdir}/gcj/%{name}/junitruntime.jar.*
%{_libdir}/gcj/%{name}/junitsupport.jar.*
%{_libdir}/gcj/%{name}/jdimodel.jar.*
%{_libdir}/gcj/%{name}/jdi.jar.*
%endif

%files jdt-sdk
%defattr(-,root,root)
%{_datadir}/%{name}/features/org.eclipse.jdt.source_*
%{_libdir}/%{name}/plugins/org.eclipse.jdt.doc.isv_*
%{_datadir}/%{name}/plugins/org.eclipse.jdt.source_*

%files pde
%defattr(-,root,root)
%{_datadir}/%{name}/features/org.eclipse.pde_*
%{_libdir}/%{name}/plugins/org.eclipse.pde.doc.user_*
%{_datadir}/%{name}/plugins/org.eclipse.pde.build_*
%{_datadir}/%{name}/plugins/org.eclipse.pde.build
%{_datadir}/%{name}/plugins/org.eclipse.pde_*
%{_datadir}/%{name}/plugins/org.eclipse.pde.core_*
%{_datadir}/%{name}/plugins/org.eclipse.pde.junit.runtime_*
%{_datadir}/%{name}/plugins/org.eclipse.pde.ui_*
%{_datadir}/%{name}/buildscripts
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.pde_*
%{_libdir}/gcj/%{name}/org.eclipse.pde.core_*
%{_libdir}/gcj/%{name}/org.eclipse.pde.junit.runtime_*
%{_libdir}/gcj/%{name}/org.eclipse.pde.ui_*
%{_libdir}/gcj/%{name}/pdebuild.jar*
%{_libdir}/gcj/%{name}/pdebuild-ant.jar*
%endif

%files pde-runtime
%defattr(-,root,root)
%{_datadir}/%{name}/plugins/org.eclipse.pde.runtime_*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.pde.runtime_*
%endif

%files pde-sdk
%defattr(-,root,root)
%{_datadir}/%{name}/features/org.eclipse.pde.source_*
%{_datadir}/%{name}/plugins/org.eclipse.pde.source_*

%files sdk
%defattr(-,root,root)
%{_libdir}/%{name}/features/org.eclipse.sdk_*
%{_libdir}/%{name}/plugins/org.eclipse.sdk_*



