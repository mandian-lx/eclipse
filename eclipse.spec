%{?_javapackages_macros:%_javapackages_macros}
%{?scl:%scl_package eclipse}
%{!?scl:%global pkg_name %{name}}
%{!?scl:%global _scl_root %{nil}}

Epoch:                  1

%global eclipse_major   4
%global eclipse_minor   3
%global eclipse_majmin  %{eclipse_major}.%{eclipse_minor}
%global eclipse_micro   1
%global initialize      1
%global eb_commit       79dfa1abc0ba06375b42d0015c7f0ceb3759eb5b
%global eclipse_tag     R4_3_1
%global eclipse_version %{eclipse_majmin}.%{eclipse_micro}
%global installation_loc %{_libdir}/%{pkg_name}

%global _jetty_version 9
%{?scl:%global _jetty_version 8}

%ifarch %{ix86}
    %define  eclipse_arch x86
%endif
%ifarch %{arm}
    %define eclipse_arch arm
%endif 
%ifarch %{power64} 
    %define eclipse_arch ppc64
%endif
%ifarch s390 s390x ppc x86_64
    %define eclipse_arch %{_arch}
%endif

# FIXME:  update java packaging guidelines for this.  See
# fedora-devel-java-list discussion in September 2008.
#
# Prevent brp-java-repack-jars from being run.
%define __jar_repack 0
%define __jar_repack %{nil}

#Usage
# _secondary baseArch targetArch
%define _secondary() \
_f=`ls | grep -e "%{1}$"`; \
if [ -d ${_f/%{2}/%{3}/} ]; then \
    echo "fragment ${_f/%{2}/%{3}/} already exists" \
else cp -r ${_f} ${_f/%{2}/%{3}/} ; \
find ${_f/%{2}/%{3}/} -type f -exec sed -i -e "s/%{2}/%{3}/g" {} \\; \
fi;


Summary:        An open, extensible IDE
Name:           %{?scl_prefix}eclipse
Version:        %{eclipse_version}
Release:        11.4%{?dist}
License:        EPL

URL:            http://www.eclipse.org/
Group:			Development/Java			
#get-eclipse.sh
Source0:        R4_platform-aggregator-%{eclipse_tag}.tar.xz
#http://git.eclipse.org/c/linuxtools/org.eclipse.linuxtools.eclipse-build.git/snapshot/org.eclipse.linuxtools.eclipse-build-701400b0ca475ea73bd828c66b00fb63c5ec2c8c.tar.bz2
Source1:        eclipse-build-%{eb_commit}.tar.xz

# -com.sun.el
# +javax.el
# -org.apache.jasper.glassfish
# +org.glassfish.web.javax.servlet.jsp
Patch0:         %{pkg_name}-help-doc-adjust-dependencies.patch

# -org.w3c.dom.smil
# -javax.annotation
# +org.apache.geronimo.specs.geronimo-annotation_1.1_spec
Patch1:         %{pkg_name}-remove-w3c-smil-and-use-geronimo.patch

# Eclipse should not duplicate dependency sources (which are delivered
# by those dependencies packages).
Patch3:         %{pkg_name}-no-source-for-dependencies.patch

# This has too many dependencies. We will not build it.
Patch4:         %{pkg_name}-remove-weaving.patch

# https://bugs.eclipse.org/bugs/show_bug.cgi?id=385970
Patch5:        %{pkg_name}-osgi-unpack-sources.patch

# https://bugs.eclipse.org/bugs/show_bug.cgi?id=379102
Patch6:        %{pkg_name}-do-not-run-as-root.patch

# https://bugs.eclipse.org/bugs/show_bug.cgi?id=377515
Patch7:        %{pkg_name}-p2-pick-up-renamed-jars.patch

# Patch for this was contributed. Unlikely to be released.
Patch8:        %{pkg_name}-ignore-version-when-calculating-home.patch

# CBI uses timestamps generated from the git commits. We don't have the repo,
# just source, and we don't want additional dependencies.
Patch9:        %{pkg_name}-remove-jgit-provider.patch

# This is for Fedora purposes to have working eclipse-pdebuild script.
Patch10:        %{pkg_name}-pdebuild-add-target.patch

# Strict Fedora purpose, too. We can't build entire product, just base
# and JDT and SDK as update sites, then we can assemble our own packages.
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=386670
# additional poms are a part of e-b
Patch11:        %{pkg_name}-change-build-packagings.patch

Patch14:        %{pkg_name}-test-support.patch

Patch17:        %{pkg_name}-secondary-arches.patch

Patch18:        %{pkg_name}-debug-symbols.patch

Patch20:        %{pkg_name}-fix-comaptibility-class.patch

Patch21:		%{pkg_name}-fix-swt-build-in-rawhide.patch

Patch22:		%{pkg_name}-bug-903537.patch

Patch23:		%{pkg_name}-jetty-9.patch

Patch25:		%{pkg_name}-fix-startup-class-refresh.patch

Patch26:		%{pkg_name}-fix-dropins.patch

Patch27:		%{pkg_name}-bug-408505.patch

Patch29:		%{pkg_name}-bug-386377.patch

BuildRequires: ant >= 1.8.3
BuildRequires: rsync
BuildRequires: jpackage-utils >= 0:1.5, make, gcc
%if 0%{?fedora}
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: glib2-devel
%else
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(glib-2.0)
%endif
BuildRequires: GConf2-devel
BuildRequires: gcc-c++
BuildRequires: nspr-devel
%if 0%{?fedora}
BuildRequires: libXtst-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: cairo >= 1.0
%else
BuildRequires: libxtst-devel
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(cairo)
%endif
BuildRequires: unzip
BuildRequires: coreutils
BuildRequires: desktop-file-utils
BuildRequires: java-devel >= 1:1.7.0
BuildRequires: java-javadoc >= 1:1.7.0
%if 0%{?fedora}
BuildRequires: libXt-devel
BuildRequires: webkitgtk-devel
BuildRequires: webkitgtk3
%else
BuildRequires: libxt-devel
BuildRequires: pkgconfig(webkit-1.0)
BuildRequires: pkgconfig(webkitgtk-3.0)
%endif
BuildRequires: geronimo-annotation >= 1.0-7
BuildRequires: %{?scl_prefix}icu4j-eclipse >= 1:50.1.1
BuildRequires: ant-antlr ant-apache-bcel ant-apache-log4j ant-apache-oro ant-apache-regexp ant-apache-resolver ant-commons-logging ant-apache-bsf ant-commons-net
BuildRequires: ant-javamail ant-jdepend ant-junit ant-swing ant-jsch ant-testutil ant-apache-xalan2 ant-jmf
BuildRequires: ant-scripts
BuildRequires: jsch >= 0:0.1.46-2
BuildRequires: apache-commons-el >= 1.0-22
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-codec >= 1.6-2
BuildRequires: %{?scl_prefix}felix-gogo-command >= 0.12
BuildRequires: %{?scl_prefix}felix-gogo-shell >= 0.10.0-3
BuildRequires: osgi(org.eclipse.jetty.util) >= %{_jetty_version}
BuildRequires: osgi(org.eclipse.jetty.server) >= %{_jetty_version}
BuildRequires: osgi(org.eclipse.jetty.http) >= %{_jetty_version}
BuildRequires: osgi(org.eclipse.jetty.continuation) >= %{_jetty_version}
BuildRequires: osgi(org.eclipse.jetty.io) >= %{_jetty_version}
BuildRequires: osgi(org.eclipse.jetty.security) >= %{_jetty_version}
BuildRequires: osgi(org.eclipse.jetty.servlet) >= %{_jetty_version}
BuildRequires: lucene >= 2.9.4-8
BuildRequires: lucene-contrib >= 2.9.4-8
BuildRequires: junit >= 4.10-5
BuildRequires: hamcrest >= 0:1.1-11
BuildRequires: %{?scl_prefix}sat4j >= 2.3.5-1
BuildRequires: objectweb-asm >= 3.3.1-1
BuildRequires: zip
BuildRequires: sac >= 1.3-12
BuildRequires: batik  >= 1.8
BuildRequires: xml-commons-apis >= 1.4.01-12
BuildRequires: atinject >= 1-6
BuildRequires: tycho >= 0.16
BuildRequires: tycho-extras >= 0.16
BuildRequires: eclipse-emf-core >= 1:2.9.0-1
BuildRequires: %{?scl_prefix}eclipse-ecf-core >= 3.6.0-2
BuildRequires: tomcat-servlet-3.0-api
BuildRequires: tomcat-el-2.2-api
BuildRequires: glassfish-jsp-api >= 2.2.1-4
BuildRequires: cglib
BuildRequires: glassfish-jsp >= 2.2.5
BuildRequires: cbi-plugins
BuildRequires: xml-maven-plugin
BuildRequires: mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires: maven-deploy-plugin
BuildRequires: httpcomponents-core
BuildRequires: httpcomponents-client
BuildRequires: eclipse-egit
BuildRequires: eclipse-jgit
BuildRequires: eclipse-pde
%if 0%{?rhel} >= 6
ExclusiveArch: %{ix86} x86_64
%endif

%description
The Eclipse platform is designed for building integrated development
environments (IDEs), server-side applications, desktop applications, and
everything in between.

%package     swt
Version:        %{eclipse_version}
Summary:        SWT Library for GTK+

# %%{_libdir}/java directory owned by jpackage-utils
Requires:       java >= 1:1.7.0
Requires:       jpackage-utils
Requires:       gtk2
%if 0%{?fedora}
Requires:       gtk3
Requires:       webkitgtk
Requires:       webkitgtk3
%else
Requires:       gtk+3
Requires:       webkit1.0
Requires:       webkit3.0
%endif

%description swt
SWT Library for GTK+.

%package      equinox-osgi
Version:        %{eclipse_version}
Summary:        Eclipse OSGi - Equinox
Requires:       java >= 1:1.7.0
Requires:       jpackage-utils
Provides:       osgi(system.bundle) = %{epoch}:%{eclipse_version}

%description  equinox-osgi
Eclipse OSGi - Equinox

%package        platform
Version:        %{eclipse_version}
Summary:        Eclipse platform common files

Requires: ant-antlr ant-apache-bcel ant-apache-log4j ant-apache-oro ant-apache-regexp ant-apache-resolver ant-commons-logging ant-apache-bsf ant-commons-net
Requires: ant-javamail ant-jdepend ant-junit ant-swing ant-jsch ant-testutil ant-apache-xalan2 ant-jmf
Requires: ant-scripts
Requires: apache-commons-el >= 1.0-23
Requires: apache-commons-logging
Requires: apache-commons-codec >= 1.6-2
Requires: %{?scl_prefix}felix-gogo-command >= 0.12
Requires: %{?scl_prefix}felix-gogo-shell >= 0.10.0-3
Requires: osgi(org.eclipse.jetty.util) >= %{_jetty_version}
Requires: osgi(org.eclipse.jetty.server) >= %{_jetty_version}
Requires: osgi(org.eclipse.jetty.http) >= %{_jetty_version}
Requires: osgi(org.eclipse.jetty.continuation) >= %{_jetty_version}
Requires: osgi(org.eclipse.jetty.io) >= %{_jetty_version}
Requires: osgi(org.eclipse.jetty.security) >= %{_jetty_version}
Requires: osgi(org.eclipse.jetty.servlet) >= %{_jetty_version}
Requires: jsch >= 0.1.46-2
Requires: lucene >= 2.9.4-8
Requires: lucene-contrib >= 2.9.4-8
Requires: %{?scl_prefix}sat4j >= 2.3.5-1
Requires: sac >= 1.3-12
Requires: xml-commons-apis >= 1.4.01-12
Requires: batik >= 1.8
Requires: atinject >= 1-6
Requires: geronimo-annotation >= 1.0-7
Requires: %{?scl_prefix}eclipse-ecf-core >= 3.6.0-2
Requires: eclipse-emf-core >= 2.9.0-1
Requires: tomcat-servlet-3.0-api
Requires: tomcat-el-2.2-api
Requires: glassfish-jsp-api >= 2.2.1-4
Requires: glassfish-jsp >= 2.2.5
Requires: %{?scl_prefix}icu4j-eclipse >= 1:50.1.1
Requires: %{name}-swt = %{epoch}:%{eclipse_version}-%{release}
Requires: %{name}-equinox-osgi = %{epoch}:%{eclipse_version}-%{release}
Requires: httpcomponents-core
Requires: httpcomponents-client
%{?scl:Requires: %scl_runtime}
Provides: %{name}-cvs-client = %{epoch}:%{eclipse_version}-%{release}
Obsoletes: %{name}-cvs-client < 1:3.3.2-20
Obsoletes: %{name}-rcp < 1:4.3.0
Provides: %{name}-rcp = 1:%{eclipse_version}-%{release}

%description    platform
The Eclipse Platform is the base of all IDE plugins.  This does not include the
Java Development Tools or the Plugin Development Environment.

%package        jdt
Version:        %{eclipse_version}
Summary:        Eclipse Java Development Tools

Requires:       %{name}-platform = %{epoch}:%{eclipse_version}-%{release}
Requires:       %{name}-cvs-client = %{epoch}:%{eclipse_version}-%{release}
Requires:       junit >= 4.10-5
Requires:       hamcrest >= 0:1.1-11
Requires:       java-javadoc >= 1:1.7.0


%description    jdt
Eclipse Java Development Tools.  This package is required to use Eclipse for
developing software written in the Java programming language.

%package        pde
Version:        %{eclipse_version}
Summary:        Eclipse Plugin Development Environment

Provides:       %{name} = %{epoch}:%{eclipse_version}-%{release}
Provides:       %{name}-sdk = %{epoch}:%{eclipse_version}-%{release}
Requires:       %{name}-platform = %{epoch}:%{eclipse_version}-%{release}
Requires:       %{name}-jdt = %{epoch}:%{eclipse_version}-%{release}
Requires:       objectweb-asm >= 3.3.1-1
# For PDE Build wrapper script + creating jars
Requires:       zip
Requires:       bash
Provides:       %{name}-pde-runtime = 1:%{eclipse_version}-%{release}
Obsoletes:      %{name}-pde-runtime < 1:3.3.2-20

%description    pde
Eclipse Plugin Development Environment.  This package is required for
developing Eclipse plugins.

%package        tests
Version:        %{eclipse_version}
Summary:        Eclipse Tests

Requires:       %{name}-pde = %{epoch}:%{eclipse_version}-%{release}
Requires:		%{?scl_prefix}easymock3

%description    tests
Eclipse Tests.

%prep

%setup -q %{SOURCE0} -n R4_platform-aggregator-%{eclipse_tag}

tar --strip-components=1 -xf %{SOURCE1} 

%patch0
%patch1
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9
%patch10
%patch11
%patch14
%patch17
%patch18
%patch20
%patch21
%patch22
%{!?scl:%patch23}
%patch25
%patch26
%patch27
pushd rt.equinox.framework
%patch29 -p1
popd

#Disable as many things as possible to make the build faster. We care only for Eclipse.
%pom_disable_module platform.sdk eclipse.platform.releng.tychoeclipsebuilder
%pom_disable_module rcp eclipse.platform.releng.tychoeclipsebuilder
%pom_disable_module rcp.sdk eclipse.platform.releng.tychoeclipsebuilder
%pom_disable_module sdk eclipse.platform.releng.tychoeclipsebuilder
%pom_disable_module equinox.starterkit.product eclipse.platform.releng.tychoeclipsebuilder
%pom_disable_module osgistarter.config.launcher eclipse.platform.releng.tychoeclipsebuilder
%pom_disable_module eclipse.platform.repository

%pom_disable_module bundles/org.eclipse.equinox.region.tests rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.weaving.aspectj rt.equinox.bundles
%pom_disable_module features/org.eclipse.equinox.weaving.sdk rt.equinox.bundles
%pom_disable_module features/master-equinox-weaving eclipse.platform.releng
%pom_disable_module bundles/org.eclipse.equinox.cm.test rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.console.ssh rt.equinox.bundles

%pom_disable_module features/org.eclipse.equinox.sdk rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.console.jaas.fragment rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.ip rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.transforms.xslt rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.transforms.hook rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.weaving.caching.j9 rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.weaving.caching rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.weaving.hook rt.equinox.bundles
%pom_disable_module features/org.eclipse.equinox.compendium.sdk rt.equinox.bundles
%pom_disable_module features/org.eclipse.equinox.core.sdk rt.equinox.framework
%pom_disable_module features/org.eclipse.equinox.p2.sdk rt.equinox.p2
%pom_disable_module features/org.eclipse.equinox.server.p2 rt.equinox.bundles
%pom_disable_module features/org.eclipse.equinox.serverside.sdk rt.equinox.bundles
%pom_disable_module features/master-equinox eclipse.platform.releng
%pom_disable_module features/master eclipse.platform.releng
%pom_disable_module bundles/org.eclipse.releng.tools eclipse.platform.releng
%pom_disable_module bundles/org.eclipse.releng.tests eclipse.platform.releng
%pom_disable_module features/org.eclipse.releng.tools eclipse.platform.releng
%pom_disable_module bundles/org.eclipse.equinox.p2.tests.discovery rt.equinox.p2

%pom_disable_module bundles/org.eclipse.swt.gtk.aix.ppc eclipse.platform.swt.binaries
%pom_disable_module bundles/org.eclipse.swt.gtk.aix.ppc64 eclipse.platform.swt.binaries
%pom_disable_module bundles/org.eclipse.swt.gtk.solaris.sparc eclipse.platform.swt.binaries
%pom_disable_module bundles/org.eclipse.swt.gtk.solaris.x86 eclipse.platform.swt.binaries
%pom_disable_module bundles/org.eclipse.swt.gtk.hpux.ia64 eclipse.platform.swt.binaries


# Use our system-installed javadocs, reference only what we built, and
# don't like to osgi.org docs (FIXME:  maybe we should package them?)
sed -i -e "s|http://download.oracle.com/javase/6/docs/api|%{_datadir}/javadoc/java|" \
   -e "/osgi\.org/d" \
   -e "s|-breakiterator|;../org.eclipse.equinox.util/@dot\n;../org.eclipse.ecf.filetransfer_3.0.0.v20090302-0803.jar\n;../org.eclipse.ecf_3.0.0.v20090302-0803.jar\n-breakiterator|" \
    eclipse.platform.common/bundles/org.eclipse.platform.doc.isv/platformOptions.txt
sed -i -e "s|http://download.oracle.com/javase/6/docs/api|%{_datadir}/javadoc/java|" \
   -e "s/win32.win32.x86/gtk.linux.%{eclipse_arch}/" \
   eclipse.platform.common/bundles/org.eclipse.jdt.doc.isv/jdtOptions.txt
sed -i -e "s|http://download.oracle.com/javase/6/docs/api|%{_datadir}/javadoc/java|" \
   -e "/osgi\.org/d" \
   eclipse.platform.common/bundles/org.eclipse.jdt.doc.isv/jdtOptions.txt
sed -i -e "s|http://download.oracle.com/javase/1.4.2/docs/api|%{_datadir}/javadoc/java|" \
   -e "s/motif.linux.x86/gtk.linux.%{eclipse_arch}/" \
   -e "/osgi\.org/d" \
   eclipse.platform.common/bundles/org.eclipse.pde.doc.user/pdeOptions.txt \
   eclipse.platform.common/bundles/org.eclipse.pde.doc.user/pdeOptions.txt
sed -i -e "s|http://download.oracle.com/javase/6/docs/api|%{_datadir}/javadoc/java|" \
   eclipse.platform.common/bundles/org.eclipse.pde.doc.user/pdeOptions.txt \
   eclipse.platform.common/bundles/org.eclipse.pde.doc.user/pdeOptions.txt


#This part generates secondary fragments using primary fragments.
pushd  eclipse.platform.swt.binaries/bundles
    %_secondary gtk.linux.x86 x86 arm
    find . -name build.xml -exec sed -i -e "s/make_xulrunner//g" {} \;
    find . -name build.xml -exec sed -i -e "s/make_mozilla//g" {} \;
    find . -name build.xml -exec sed -i -e "s/make_xpcominit//g" {} \;
popd 
pushd eclipse.platform.resources/bundles
    %_secondary linux.x86 x86 arm
    %_secondary linux.x86 x86 s390
    %_secondary linux.x86_64 x86_64 s390x
popd
pushd eclipse.platform.team/bundles/org.eclipse.core.net/fragments
    %_secondary linux.x86 x86 arm
    %_secondary linux.x86 x86 ppc
    %_secondary linux.x86_64 x86_64 ppc64
    %_secondary linux.x86 x86 s390
    %_secondary linux.x86_64 x86_64 s390x
popd
pushd rt.equinox.framework/bundles
    %_secondary gtk.linux.x86 x86 arm
popd
pushd rt.equinox.binaries
    %_secondary gtk.linux.x86 x86 arm
popd

#hack - there should be a patch providing a profile for each arch
mkdir -p rt.equinox.framework/bundles/org.eclipse.equinox.executable/bin/gtk/linux/%{eclipse_arch}
mkdir -p rt.equinox.binaries/org.eclipse.equinox.executable/bin/gtk/linux/%{eclipse_arch}

#pdebuild script should point to dropins
sed -i -e "s|@DATADIR@|%{_datadir}|g" eclipse.pde.build/org.eclipse.pde.build/templates/package-build/build.properties


#ensure that bundles with *.so libs are dirs, so no *.so is extracted into user.home
for f in `find eclipse.platform.swt.binaries/bundles/org.eclipse.swt.gtk.* -name MANIFEST.MF` ; do 
	echo -e "Eclipse-BundleShape: dir\n\n" >> $f; 
done
for f in `find eclipse.platform.resources/bundles/org.eclipse.core.filesystem.linux.* -name MANIFEST.MF` ; do 
	echo -e "Eclipse-BundleShape: dir\n\n" >> $f; 
done
for f in `find eclipse.platform.team/bundles/org.eclipse.core.net/fragments -name MANIFEST.MF` ; do 
	echo -e "Eclipse-BundleShape: dir\n\n" >> $f; 
done

#fake dependencies that don't exist in fedora
./dependencies/./fake_ant_dependency.sh .m2/p2/repo-sdk/plugins/org.apache.ant_* /usr/share/java /usr/bin -makejar

cp -r /usr/share/java/emf/eclipse/features/* .m2/p2/repo-sdk/features/
%{?scl: cp %{_javadir}/ecf/eclipse/plugins/* .m2/p2/repo-sdk/plugins}
%{?scl: cp %{_javadir}/*sat4j* .m2/p2/repo-sdk/plugins}
cp -rf %{_libdir}/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_* .m2/p2/repo-sdk/plugins/
cp -rf %{_libdir}/eclipse/dropins/sdk/plugins/org.eclipse.pde.core_* .m2/p2/repo-sdk/plugins/

%pom_remove_plugin  org.mortbay.jetty:jetty-jspc-maven-plugin  eclipse.platform.ua/org.eclipse.help.webapp
%pom_remove_plugin  org.eclipse.tycho:tycho-compiler-plugin rt.equinox.p2/org.eclipse.equinox.p2.releng/org.eclipse.equinox.p2-parent

find eclipse.platform.ua -name pom.xml -exec sed -i -e 's@org.apache.lucene<@org.apache.lucene.core<@g' {} \;

#this is not really necessary but reduces the build time.
pushd eclipse.platform.swt.binaries/bundles/
	for bundle in `ls | grep "org.eclipse.swt" | grep -v -e "org.eclipse.swt.gtk.linux.%{eclipse_arch}$"` ; do
		if [ -e $bundle/pom.xml ]; then
			%pom_xpath_remove "/pom:project/pom:build" $bundle/pom.xml
		fi 
	done
popd

sed -i -e 's@Dhelp.lucene.tokenizer=standard@XX:MaxPermSize=384M@g' eclipse.platform.common/bundles/org.eclipse.platform.doc.isv/pom.xml
%build
%{?scl:%scl_maven_opts}
#This is the lowest value where the build succeeds. 512m is not enough.
export MAVEN_OPTS="-Xmx900m -XX:CompileCommand=exclude,org/eclipse/tycho/core/osgitools/EquinoxResolver,newState ${MAVEN_OPTS}"
export JAVA_HOME=%{java_home}

pushd eclipse.platform.swt.binaries/bundles/org.eclipse.swt.gtk.linux.%{eclipse_arch}
	mvn-rpmbuild clean verify \
   -Dmaven.test.skip=true -Dnative=gtk.linux.%{eclipse_arch} -DskipTychoVersionCheck \
   -Dtycho.local.keepTarget -Dmaven.repo.local=../../../.m2
popd

export GTK_VERSION=3.0
mvn-rpmbuild clean verify -P update-branding-plugins \
   -Dmaven.test.skip=true -Dnative=gtk.linux.%{eclipse_arch} -DskipTychoVersionCheck \
   -Dtycho.local.keepTarget -DbuildId=`echo "%{release}" | tr -d "."`

# XMvn may places jars differently from mvn-rpmbuild
sed -i 's/glassfish-jsp-api\.jar/glassfish-jsp-api\/javax\.servlet\.jsp-api\.jar/' dependencies/./replace_platform_plugins_with_symlinks.sh
sed -i 's/felix\/org\.apache\.felix\.gogo\.runtime\.jar/felix\/felix-gogo-runtime\.jar/' dependencies/./replace_platform_plugins_with_symlinks.sh

#symlink necessary plugins (that are provided by other packages)
dependencies/./replace_platform_plugins_with_symlinks.sh \
	eclipse.platform.releng.tychoeclipsebuilder/platform/target/products/org.fedoraproject.eclipse.platform/linux/gtk/%{eclipse_arch}/eclipse %{_javadir}
#ant again
./dependencies/./fake_ant_dependency.sh \
	 eclipse.platform.releng.tychoeclipsebuilder/platform/target/products/org.fedoraproject.eclipse.platform/linux/gtk/%{eclipse_arch}/eclipse/plugins/org.apache.ant_* /usr/share/java \
     /usr/bin

# JDT and PDE are built as update sites.
# Initialize them and move into dropins.
utils/./move_JDT_PDE_to_dropins.sh \
eclipse.platform.releng.tychoeclipsebuilder/platform/target/products/org.fedoraproject.eclipse.platform/linux/gtk/%{eclipse_arch}/ \
`pwd`/eclipse.platform.releng.tychoeclipsebuilder/jdtpde/target/repository

pushd eclipse.platform.releng.tychoeclipsebuilder/platform/target/products/org.fedoraproject.eclipse.platform/linux/gtk/%{eclipse_arch}/eclipse

#in jdt and pde
pushd dropins/jdt/plugins
 f=`ls | grep -e "^org.hamcrest.core_"`
 rm -f $f 
 ln -s %{_javadir}/hamcrest/core.jar $f

 rm -rf org.junit_4*
 ln -s /usr/share/java/junit.jar
popd
pushd dropins/sdk/plugins
 f=`ls | grep -e "^org.objectweb.asm_"`
 rm $f 
 ln -s %{_javadir}/objectweb-asm/asm-all.jar $f
popd

#clean up
rm -rf configuration/org.eclipse.core.runtime
rm -rf configuration/org.eclipse.equinox.app
rm -rf configuration/org.eclipse.update
rm -rf configuration/org.eclipse.osgi
rm -rf p2/org.eclipse.equinox.p2.core/cache/*
# no icon needed
rm -f icon.xpm

#delete all local repositories. We want to have only "original" by default.
pushd p2/org.eclipse.equinox.p2.engine/.settings
    sed -i "/repositories\/file/d" *.prefs ../profileRegistry/SDKProfile.profile/.data/.settings/*.prefs
    sed -i "/repositories\/memory/d" *.prefs ../profileRegistry/SDKProfile.profile/.data/.settings/*.prefs
popd

#ini file adjustements
# Temporary fix until https://bugs.eclipse.org/294877 is resolved
sed -i "s|-Xms40m|-Xms128m|g" eclipse.ini
sed -i "s|-Xmx384m|-Xmx512m|g" eclipse.ini
sed -i '1i-preventMasterEclipseLaunch' eclipse.ini

cat >> eclipse.ini <<EOF
-Dorg.eclipse.swt.browser.UseWebKitGTK=true
-Dhelp.lucene.tokenizer=standard
-XX:CompileCommand=exclude,org/eclipse/core/internal/dtree/DataTreeNode,forwardDeltaWith
-XX:CompileCommand=exclude,org/eclipse/jdt/internal/compiler/lookup/ParameterizedMethodBinding,<init>
-XX:CompileCommand=exclude,org/eclipse/cdt/internal/core/dom/parser/cpp/semantics/CPPTemplates,instantiateTemplate
-XX:CompileCommand=exclude,org/eclipse/cdt/internal/core/pdom/dom/cpp/PDOMCPPLinkage,addBinding
-XX:CompileCommand=exclude,org/python/pydev/editor/codecompletion/revisited/PythonPathHelper,isValidSourceFile
-XX:CompileCommand=exclude,org/eclipse/tycho/core/osgitools/EquinoxResolver,newState
-Dorg.eclipse.equinox.p2.reconciler.dropins.directory=%{_scl_root}/usr/share/eclipse/dropins
-Declipse.p2.skipMovedInstallDetection=true
--launcher.GTK_version
2
EOF

popd #eclipse

%install

#install icons
install -D eclipse.platform/platform/org.eclipse.platform/eclipse32.png \
    $RPM_BUILD_ROOT/usr/share/icons/hicolor/32x32/apps/%{?scl_prefix}eclipse.png
install -D eclipse.platform/platform/org.eclipse.platform/eclipse48.png \
    $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps/%{?scl_prefix}eclipse.png
install -D eclipse.platform/platform/org.eclipse.platform/eclipse256.png \
    $RPM_BUILD_ROOT/usr/share/icons/hicolor/256x256/apps/%{?scl_prefix}eclipse.png
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps/ 
ln -s /usr/share/icons/hicolor/256x256/%{?scl_prefix}apps/eclipse.png \
    $RPM_BUILD_ROOT/usr/share/pixmaps/%{?scl_prefix}eclipse.png

#desktop file
%{?scl: sed -i -e 's/Exec=eclipse/Exec=scl enable %{scl_name} eclipse/g' desktopintegration/eclipse.desktop}
%{?scl: sed -i -e 's/Icon=eclipse/Icon=%{?scl_prefix}eclipse/g' desktopintegration/eclipse.desktop}
%{?scl: sed -i -e 's/Name=Eclipse/Name=DTS Eclipse/g' desktopintegration/eclipse.desktop}
install -D desktopintegration/eclipse.desktop $RPM_BUILD_ROOT/usr/share/applications/%{?scl_prefix}eclipse.desktop
install -D desktopintegration/eclipse.appdata.xml $RPM_BUILD_ROOT/usr/share/appdata/%{?scl_prefix}eclipse.appdata.xml

# Some directories we need
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/java
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{pkg_name}
install -d -m 755 $RPM_BUILD_ROOT%{_scl_root}/usr/share/%{pkg_name}/dropins
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

#################################
### Extraced from old build.xml #
#################################
LOCAL_PWD=`pwd`
#change the installation p2 files
pushd eclipse.platform.releng.tychoeclipsebuilder/platform/target/products/org.fedoraproject.eclipse.platform/linux/gtk/%{eclipse_arch}/eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/SDKProfile.profile/
for i in `ls | grep "profile.gz"` ; do  \
        echo $i ; \
        gunzip $i ; \
        sed -i -e "s@${LOCAL_PWD}/eclipse.platform.releng.tychoeclipsebuilder/platform/target/products/org.fedoraproject.eclipse.platform/linux/gtk/%{eclipse_arch}/eclipse@%{_libdir}/eclipse@g" *.profile ; \
        gzip *.profile ; \
    done 
popd 

#installation itself - copy it into right location
rsync -vrpl eclipse.platform.releng.tychoeclipsebuilder/platform/target/products/org.fedoraproject.eclipse.platform/linux/gtk/%{eclipse_arch}/eclipse \
    $RPM_BUILD_ROOT%{_libdir}


#eclipse compiler
chmod ugo+rx jdtcompilatorscript/efj.sh
mkdir -p $RPM_BUILD_ROOT%{_scl_root}/usr/bin
install jdtcompilatorscript/efj.sh $RPM_BUILD_ROOT%{_scl_root}/usr/bin/efj
TARGET_LAUNCHER=%{installation_loc}\/plugins/`ls eclipse.platform.releng.tychoeclipsebuilder/platform/target/products/org.fedoraproject.eclipse.platform/linux/gtk/%{eclipse_arch}/eclipse/plugins | grep launcher_[0-9]*`
sed -i -e "s,@LAUNCHER@,${TARGET_LAUNCHER}," $RPM_BUILD_ROOT%{_scl_root}/usr/bin/efj

#eclipse binary
mkdir -p $RPM_BUILD_ROOT%{_scl_root}/usr/bin/
pushd $RPM_BUILD_ROOT%{_scl_root}/usr/bin/
    ln -s %{_libdir}/%{pkg_name}/eclipse
popd 

#SWT is now a folder, but we need to provide jars for others that depend on it.
pushd $RPM_BUILD_ROOT/%{_libdir}/%{pkg_name}
pushd plugins
SWT_JAR=`ls | grep swt.gtk`
#it's a dir now
cd ${SWT_JAR}
#fix privileges
#zip the contents
zip -r "../../swt.jar" *
popd
    ln -s  swt.jar swt-gtk.jar
	mkdir -p ../../lib/java
	ln -s  %{_libdir}/%{pkg_name}/swt.jar ../../lib/java/swt.jar
popd

#eclipse ini
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/
pushd $RPM_BUILD_ROOT/%{_sysconfdir}/
	ln -s %{_libdir}/%{pkg_name}/eclipse.ini
popd
#################################
### End of extraction           #
#################################

# OSGI JAR symlinks in javadir and maven depmaps
pushd $RPM_BUILD_ROOT%{_javadir}/eclipse
ln -s %{?scl: ../../../../}../../../../%{_libdir}/%{pkg_name}/plugins/org.eclipse.osgi_*.jar osgi.jar
popd
install -m 0644 externalpoms/org.eclipse.osgi-3.6.0.v20100517.pom $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.eclipse-osgi.pom
%add_maven_depmap JPP.eclipse-osgi.pom %{pkg_name}/osgi.jar -a "org.eclipse:osgi,org.eclipse.tycho:org.eclipse.osgi" -f equinox-osgi

pushd $RPM_BUILD_ROOT%{_javadir}/eclipse
ln -s %{?scl: ../../../../}../../../../%{_libdir}/%{pkg_name}/plugins/org.eclipse.osgi.services_*.jar osgi.services.jar
popd
install -m 0644 externalpoms/org.eclipse.osgi.services-3.2.100.v20100503.pom $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.eclipse-osgi.services.pom
%add_maven_depmap JPP.eclipse-osgi.services.pom %{pkg_name}/osgi.services.jar -a "org.eclipse.osgi:services" -f equinox-osgi

pushd $RPM_BUILD_ROOT%{_javadir}/eclipse
ln -s %{?scl: ../../../../}../../../../%{_libdir}/%{pkg_name}/plugins/org.eclipse.osgi.util_*.jar osgi.util.jar
popd

pushd $RPM_BUILD_ROOT%{_javadir}/eclipse
ln -s %{?scl: ../../../../}../../../../%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.http.servlet_*.jar equinox.http.servlet.jar
popd
install -m 0644 externalpoms/servlet-1.0.0-v20070606.pom $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.eclipse-equinox.http.servlet.pom
%add_maven_depmap JPP.eclipse-equinox.http.servlet.pom %{pkg_name}/equinox.http.servlet.jar -a "org.eclipse.equinox.http:servlet" -f platform

pushd $RPM_BUILD_ROOT%{_javadir}/eclipse
ln -s %{?scl: ../../../../}../../../../%{_libdir}/%{pkg_name}/plugins/org.eclipse.jdt.core_*.jar jdt.core.jar

popd
install -m 0644 externalpoms/org.eclipse.jdt.core-3.8.0.v_C03.pom $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.eclipse-jdt.core.pom
%add_maven_depmap JPP.eclipse-jdt.core.pom %{pkg_name}/jdt.core.jar -a "org.eclipse:jdt.core,org.eclipse.tycho:org.eclipse.jdt.core,org.eclipse.jetty.orbit:org.eclipse.jdt.core,org.eclipse.jdt:org.eclipse.jdt.core"  -f jdt
# A sanity check.
desktop-file-validate %{buildroot}/usr/share/applications/%{name}.desktop

# Create a script that can be used to make a symlink tree of the
# eclipse platform.
cp -p pdebuildscripts/eclipse-copy-platform.sh copy-platform
sed -i -e "s|@DATADIR@|%{_datadir}|g" copy-platform

mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{pkg_name}/buildscripts
mv copy-platform $RPM_BUILD_ROOT%{_libdir}/%{pkg_name}/buildscripts
copyPlatform=$RPM_BUILD_ROOT%{_libdir}/%{pkg_name}/buildscripts/copy-platform

# Install the PDE Build wrapper script.
install -p -D -m0755 pdebuildscripts/eclipse-pdebuild.sh \
  $RPM_BUILD_ROOT%{_bindir}/%{pkg_name}-pdebuild
PDEBUILDVERSION=$(ls $RPM_BUILD_ROOT%{_libdir}/%{pkg_name}/dropins/sdk/plugins \
  | grep org.eclipse.pde.build_ | \
  sed 's/org.eclipse.pde.build_//')
sed -i "s/@PDEBUILDVERSION@/$PDEBUILDVERSION/g" \
  $RPM_BUILD_ROOT%{_bindir}/%{pkg_name}-pdebuild
sed -i "s|@LIBDIR@|%{_libdir}|g" \
  $RPM_BUILD_ROOT%{_bindir}/eclipse-pdebuild

#fix pde permissions
chmod a+x  $RPM_BUILD_ROOT%{_libdir}/%{pkg_name}/dropins/sdk/plugins/org.eclipse.pde.build_*/templates/package-build/*.sh
#replace pde reference
sed -i "s@/usr/share/eclipse@%{libdir}/%{pkg_name}@" $RPM_BUILD_ROOT%{_libdir}/%{pkg_name}/dropins/sdk/plugins/org.eclipse.pde.build_*/templates/package-build/build.properties


##############
# Tests
##############

unzip eclipse.platform.releng.tychoeclipsebuilder/eclipse-junit-tests/target/eclipse-junit-tests-bundle.zip -d $RPM_BUILD_ROOT/%{_javadir}/
unzip $RPM_BUILD_ROOT/%{_javadir}/eclipse-testing/eclipse-junit-tests-*.zip -d $RPM_BUILD_ROOT/%{_javadir}/eclipse-testing
cp eclipse.platform.releng.tychoeclipsebuilder/eclipse-junit-tests/src/main/scripts/JUNIT.XSL $RPM_BUILD_ROOT/%{_javadir}/eclipse-testing
cp eclipse.platform.releng.tychoeclipsebuilder/eclipse-junit-tests/src/main/scripts/library.xml $RPM_BUILD_ROOT/%{_javadir}/eclipse-testing
cp production/testScripts/configuration/sdk.tests/testConfigs/linux/testing.properties $RPM_BUILD_ROOT/%{_javadir}/eclipse-testing
cp utils/splitter.xsl $RPM_BUILD_ROOT/%{_javadir}/eclipse-testing
rm $RPM_BUILD_ROOT/%{_javadir}/eclipse-testing/eclipse-junit-tests-*.zip
rm $RPM_BUILD_ROOT/%{_javadir}/eclipse-testing/runtests.bat

pushd $RPM_BUILD_ROOT/%{_javadir}/eclipse-testing/plugins
f=`ls | grep  org.easymock_`
rm $f
ln -s /usr/share/java/easymock.jar $f
rm -rf org.hamcrest.core_*
rm -rf org.junit_*
rm -rf org.junit4_*
popd

sed -i -e "s#@libdir@#%{_libdir}#" $RPM_BUILD_ROOT/%{_javadir}/eclipse-testing/runtests.sh
sed -i -e "s#@USR@#%{?scl:%{_scl_root}}%{_usr}#" $RPM_BUILD_ROOT/%{_javadir}/eclipse-testing/runtests.sh
touch $RPM_BUILD_ROOT%{_bindir}/%{pkg_name}-runEclipsePackageTests
chmod a+x  $RPM_BUILD_ROOT/%{_bindir}/%{pkg_name}-runEclipsePackageTests
echo '#!/bin/sh' >>  $RPM_BUILD_ROOT/%{_bindir}/%{pkg_name}-runEclipsePackageTests
echo 'echo "results in /tmp/eclipse-tests-directory/results/"' >>  $RPM_BUILD_ROOT/%{_bindir}/%{pkg_name}-runEclipsePackageTests
echo 'export testslocation="%{_javadir}/eclipse-testing/"' >> $RPM_BUILD_ROOT/%{_bindir}/%{pkg_name}-runEclipsePackageTests
echo "pushd %{_javadir}/eclipse-testing;./runtests.sh -os linux -ws gtk -arch %{eclipse_arch} ; popd;" >>  $RPM_BUILD_ROOT/%{_bindir}/%{pkg_name}-runEclipsePackageTests

# Package testbundle-to-eclipse-test
cp -r testbundle-to-eclipse-test $RPM_BUILD_ROOT/%{_javadir}/eclipse-testing/testbundle

pushd $RPM_BUILD_ROOT/%{_javadir}/eclipse-testing/testbundle

# Set the proper paths for scripts
sed -i 's|\.\+/\(gatherBundles\.sh\)|%{_javadir}/eclipse-testing/testbundle/\1|' prepRuntimeLocation.sh
sed -i 's|\.\+/\(genRepo\.sh\)|%{_javadir}/eclipse-testing/testbundle/\1|' prepAllTestBundles.sh
sed -i 's|\.\+/\(prepRuntimeLocation\.sh\)|%{_javadir}/eclipse-testing/testbundle/\1|' %{pkg_name}-runTestBundles
sed -i 's|\.\+/\(prepAllTestBundles\.sh\)|%{_javadir}/eclipse-testing/testbundle/\1|' %{pkg_name}-runTestBundles
sed -i 's|cp swtbot-library.xml alltest.xml updateTestBundleXML.sh target/|cp %{_javadir}/eclipse-testing/testbundle/{swtbot-library.xml,alltest.xml,updateTestBundleXML.sh} target/|' prepRuntimeLocation.sh

for file in genRepo.sh gatherBundles.sh ;do
  sed -i '/prefix=\$ROOT_PREFIX/ i ROOT_PREFIX=%{_scl_root}' ${file}
done

mv $RPM_BUILD_ROOT/%{_javadir}/eclipse-testing/testbundle/%{pkg_name}-runTestBundles $RPM_BUILD_ROOT/%{_bindir}/%{pkg_name}-runTestBundles
popd

#fix so permissions
find $RPM_BUILD_ROOT/%{_libdir}/eclipse -name *.so -exec chmod a+x {} \;

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


%files swt
%dir %{_libdir}/%{pkg_name}
%dir %{_libdir}/%{pkg_name}/plugins
%{_libdir}/%{pkg_name}/notice.html
%{_libdir}/%{pkg_name}/eclipse.ini
%{_libdir}/%{pkg_name}/epl-v10.html
%{_libdir}/%{pkg_name}/plugins/org.eclipse.swt_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.swt.gtk.linux.*
%{_libdir}/%{pkg_name}/swt-gtk*.jar
%{_libdir}/%{pkg_name}/swt.jar
%{_libdir}/../lib/java/swt.jar


%files platform -f .mfiles-platform
%attr(0755,root,root) %{_bindir}/%{pkg_name}
%{_libdir}/%{pkg_name}/.eclipseproduct
%config %{_libdir}/%{pkg_name}/eclipse.ini
%config %{_sysconfdir}/eclipse.ini
/usr/share/applications/*
/usr/share/pixmaps/
/usr/share/icons/*/*/apps/*
/usr/share/appdata/%{?scl_prefix}eclipse.appdata.xml
%{_libdir}/%{pkg_name}/eclipse
%dir %{_libdir}/%{pkg_name}/dropins
%dir %{_datadir}/%{pkg_name}/
%dir %{_datadir}/%{pkg_name}/dropins
%dir %{_libdir}/%{pkg_name}/configuration/
%{_libdir}/%{pkg_name}/configuration/config.ini
%{_libdir}/%{pkg_name}/configuration/org.eclipse.equinox.simpleconfigurator/bundles.info
%dir %{_libdir}/%{pkg_name}/features/
%{_libdir}/%{pkg_name}/features/org.eclipse.platform_*
%{_libdir}/%{pkg_name}/features/org.eclipse.e4.rcp_*
%{_libdir}/%{pkg_name}/features/org.eclipse.rcp_*
%{_libdir}/%{pkg_name}/features/org.eclipse.emf.common_*
%{_libdir}/%{pkg_name}/features/org.eclipse.emf.ecore_*
%{_libdir}/%{pkg_name}/features/org.eclipse.rcp.configuration_*
%{_libdir}/%{pkg_name}/plugins/com.ibm.icu_*
%{_libdir}/%{pkg_name}/plugins/com.jcraft.jsch_*
%{_libdir}/%{pkg_name}/plugins/javax.servlet_*
%{_libdir}/%{pkg_name}/plugins/javax.servlet.jsp_*
%{_libdir}/%{pkg_name}/plugins/javax.xml_*
%{_libdir}/%{pkg_name}/plugins/javax.el_*
%{_libdir}/%{pkg_name}/plugins/javax.inject_*.jar
%{_libdir}/%{pkg_name}/plugins/org.apache.ant_*
%{_libdir}/%{pkg_name}/plugins/org.apache.batik.css_*
%{_libdir}/%{pkg_name}/plugins/org.apache.batik.util.gui_*
%{_libdir}/%{pkg_name}/plugins/org.apache.batik.util_*
%{_libdir}/%{pkg_name}/plugins/org.apache.commons.codec_*
%{_libdir}/%{pkg_name}/plugins/org.apache.httpcomponents.httpclient_*
%{_libdir}/%{pkg_name}/plugins/org.apache.httpcomponents.httpcore_*
%{_libdir}/%{pkg_name}/plugins/org.apache.commons.logging_*
%{_libdir}/%{pkg_name}/plugins/org.apache.felix.gogo.command_*
%{_libdir}/%{pkg_name}/plugins/org.apache.felix.gogo.runtime_*
%{_libdir}/%{pkg_name}/plugins/org.apache.felix.gogo.shell_*
%{_libdir}/%{pkg_name}/plugins/org.apache.geronimo.specs.geronimo-annotation_1.1_spec_*
%{_libdir}/%{pkg_name}/plugins/org.glassfish.web.javax.servlet.jsp_*
%{_libdir}/%{pkg_name}/plugins/org.apache.lucene.core_*
%{_libdir}/%{pkg_name}/plugins/org.apache.lucene.analysis_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ant.core_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.compare_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.compare.core_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.externaltools_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.filebuffers_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.filesystem_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.filesystem.linux.*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.net_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.net.linux.*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.resources_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.runtime.compatibility_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.runtime.compatibility.registry_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.variables_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.debug.core_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.jdt.core_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.debug.ui_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.emf.common_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.emf.ecore.change_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.emf.ecore.xmi_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.emf.ecore_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.ds_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.event_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.http.jetty_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.http.registry_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.http.servlet_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.jsp.jasper_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.jsp.jasper.registry_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.help.base_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.help.ui_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.help.webapp_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.jface.text_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.jsch.core_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.jsch.ui_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ltk.core.refactoring_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ltk.ui.refactoring_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.platform_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.platform.doc.user_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.search_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.team.core_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.team.ui_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.text_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.browser_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.cheatsheets_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.console_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.editors_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.externaltools_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.forms_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.ide_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.ide.application_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.intro_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.intro.universal_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.navigator_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.navigator.resources_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.net_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.views_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.views.properties.tabbed_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.workbench.texteditor_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.core.commands_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.core.contexts_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.core.di.extensions_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.core.di_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.core.services_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.ui.bindings_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.ui.css.core_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.ui.css.swt.theme_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.ui.css.swt_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.ui.di_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.ui.model.workbench_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.ui.services_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.ui.widgets_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.ui.workbench.addons.swt_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.ui.workbench.renderers.swt_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.ui.workbench.swt_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.ui.workbench3_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.e4.ui.workbench_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.jetty.util_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.jetty.server_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.jetty.http_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.jetty.continuation_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.jetty.io_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.jetty.security_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.jetty.servlet_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.team.cvs.core_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.cvs_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.team.cvs.ssh2_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.team.cvs.ui_*
%{_libdir}/%{pkg_name}/features/org.eclipse.cvs_*
%{_libdir}/%{pkg_name}/features/org.eclipse.help_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.frameworkadmin_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.frameworkadmin.equinox_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.simpleconfigurator.manipulator_*
%{_libdir}/%{pkg_name}/features/org.eclipse.equinox.p2.core.feature_*
%{_libdir}/%{pkg_name}/features/org.eclipse.equinox.p2.extras.feature_*
%{_libdir}/%{pkg_name}/features/org.eclipse.equinox.p2.rcp.feature_*
%{_libdir}/%{pkg_name}/features/org.eclipse.equinox.p2.user.ui_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.director_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.core_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.engine_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.jarprocessor_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.metadata_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.metadata.repository_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.artifact.repository_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.touchpoint.eclipse_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.touchpoint.natives_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.console_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.ql_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.operations_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.transport.ecf_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.ui_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.ui.importexport_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.ui.sdk_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.ui.sdk.scheduler_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.updatechecker_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.garbagecollector_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.directorywatcher_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.publisher_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.publisher.eclipse_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.repository_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.repository.tools_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.reconciler.dropins_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.updatesite_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.security_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.security.ui_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.extensionlocation_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.p2.director.app_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ecf.provider.filetransfer_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ecf.provider.filetransfer.httpclient4_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ecf.provider.filetransfer.httpclient4.ssl_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ecf.provider.filetransfer.ssl_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ecf.ssl_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ecf_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ecf.filetransfer_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ecf.identity_*
%{_libdir}/%{pkg_name}/plugins/org.sat4j.core_*
%{_libdir}/%{pkg_name}/plugins/org.sat4j.pb_*
%{_libdir}/%{pkg_name}/plugins/org.w3c.css.sac_*
%{_libdir}/%{pkg_name}/plugins/org.w3c.dom.svg_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.commands_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.contenttype_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.databinding.beans_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.databinding.observable_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.databinding.property_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.databinding_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.expressions_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.jobs_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.core.runtime_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.app_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.bidi_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.common_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.concurrent_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.console_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.launcher.gtk.linux.*_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.launcher_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.preferences_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.registry_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.simpleconfigurator_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.equinox.util_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.help_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.jface.databinding_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.jface_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.rcp_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui.workbench_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.ui_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.update.configurator_*
%{_libdir}/%{pkg_name}/readme
%{_libdir}/%{pkg_name}/about_files
%doc %{_libdir}/%{pkg_name}/about.html
%{_libdir}/%{pkg_name}/artifacts.xml
%{_libdir}/%{pkg_name}/p2

%files jdt -f .mfiles-jdt
%attr(0755,root,root) %{_bindir}/efj
%{_libdir}/%{pkg_name}/dropins/jdt

%files pde
%{_bindir}/%{pkg_name}-pdebuild
%{_libdir}/%{pkg_name}/buildscripts
%{_libdir}/%{pkg_name}/dropins/sdk

%files tests
%{_bindir}/%{pkg_name}-runEclipsePackageTests
%{_bindir}/%{pkg_name}-runTestBundles
%{_javadir}/%{pkg_name}-testing

%files equinox-osgi -f .mfiles-equinox-osgi
%dir %{_javadir}/%{pkg_name}
%{_javadir}/%{pkg_name}/osgi.util.jar
%{_libdir}/%{pkg_name}/plugins/org.eclipse.osgi_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.osgi.services_*
%{_libdir}/%{pkg_name}/plugins/org.eclipse.osgi.util_*

%changelog
* Mon Nov 4 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.1-11
- Fix the app data.

* Mon Oct 28 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.1-10
- Ignore find errors.

* Fri Oct 25 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.1-9
- Do mark *.so as executable.

* Fri Oct 25 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.1-8
- Mark *.so as executable.

* Fri Oct 18 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.1-7
- Add gnome app data.

* Wed Oct 16 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.1-6
- Fix the arm build.

* Mon Oct 14 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.1-5
- Build right launcher version.

* Fri Oct 11 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.1-4
- Rebuild to pick latest deps.

* Thu Oct 10 2013 Roland Grunberg <rgrunber@redhat.com> - 1:4.3.1-3
- Move testbundle-to-eclipse-test into eclipse-build upstream.

* Thu Oct 10 2013 Roland Grunberg <rgrunber@redhat.com> - 1:4.3.1-2
- Add testbundle-to-eclipse-test script.

* Mon Sep 30 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.1-1
- Update to 4.3.1.

* Thu Aug 29 2013 Alexander Kurtakov <akurtako@redhat.com> 1:4.3.0-13
- Let tests depend on easymock3.

* Tue Aug 27 2013 Roland Grunberg <rgrunber@redhat.com> - 1:4.3.0-12
- Update symlinks for glassfish-jsp-api and felix-gogo-runtime jars.

* Thu Aug 22 2013 Roland Grunberg <rgrunber@redhat.com> - 1:4.3.0-11.1
- Bump release.

* Mon Aug 19 2013 Alexander Kurtakov <akurtako@redhat.com> 1:4.3.0-11
- Bump release.

* Fri Aug 2 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-10
- Do really fix the arm build.
- Add buildid in the about dialog.

* Thu Aug 1 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-9
- An attempt to fix the arm build.

* Wed Jul 31 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-8
- Improve the build process.

* Mon Jul 29 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-7
- 404448 [GTK3] Images of disabled buttons are not grayed out

* Fri Jul 26 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-6
- Include latest changes in javapackages.

* Tue Jul 23 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-5
- Take ownerhsip of /usr/share/eclipse dir (RHBZ#986160).
- Include fix for Eclipse bug 408505.
- Added rpmlint builder to the fedora package.

* Mon Jul 8 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-4
- Rhbz 981905 - Use xz to compress tarball
- Fix the fetch script.
- Rebuild to pick latest deps.

* Mon Jun 24 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-3
- Consume Kepler EMF.

* Mon Jun 17 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-1
- Kepler release.

* Wed Jun 12 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.64.git84cba7
- Install JDT back for the arm build.

* Tue Jun 11 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.63.git84cba7
- Remove the 'remind me later' option from the migration wizard.

* Mon Jun 10 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.62.git84cba7
- Update to I20130605-2000.

* Thu Jun 6 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.60.git7bf397
- Fix the dropins reconciliation.

* Tue Jun 4 2013 Alexander Kurtakov <akurtako@redhat.com> 1:4.3.0-0.59.git7bf397
- Fix bogus dates and SWT description.

* Tue Jun 4 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.59.git7bf397
- Remove swt jar from plugins as it may break reconcilation.

* Thu May 30 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.58.git7bf397
- Update to daily build.

* Wed May 29 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.57.gitfde729
- Don't guess previous configuration on first install.
- Ignore version when calculating user Eclipse folder.

* Wed May 29 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.56.gitfde729
- Update to RC2.

* Thu May 23 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.55.gitbeff8a2
- Fix the testing.properties location.

* Thu May 23 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.54.gitbeff8a2
- Update to RC1.

* Mon May 20 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.53.git4bccf2
- Rebuild with latest dependencies.

* Sun May 19 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.52.git4bccf2
- Really fix the version of jdt.

* Sat May 18 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.51.git4bccf2
- Install jdt jar even for local swt local build.

* Sat May 18 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.50.git4bccf2
- Update version of jdt.

* Fri May 17 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.49.git4bccf2
- Install JDT pom manually for the purpose of secondary archs.

* Thu May 16 2013 Krzysztof Daniel <kdanie@redhat.com>  1:4.3.0-0.48.git4bccf2
- Incorporate patch for dropins issue (Bug 408138)
- Revert previous change.

* Wed May 15 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.47.git4bccf2
- Revert patches for startup issues as they cause more harm than good.

* Tue May 14 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.46.git4bccf2
- Rebuild to pick up icu4j 50.1.1.

* Mon May 13 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.45.git4bccf2
- Upload sources.

* Mon May 13 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.44.git4bccf2
- Fix the build on secondary platforms.
- Update to latest upstream.

* Mon May 13 2013 Alexander Kurtakov <akurtako@redhat.com> 1:4.3.0-0.43
- Fix the eclipse-rcp obsolete version.

* Tue May 7 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.42
- Fix tests.

* Thu May 02 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.41
- Update to latest upstream.

* Tue Apr 23 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.40
- Fix generating tests summary.
- RHBZ 955214 Failure to properly start bundle on first run.
- Eclipse Bug 406419 - Don't use -XX:-UseLoopPredicate

* Mon Apr 22 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.39
- Include a fix for a crash in libsoup/webkitgtk-2.x

* Fri Apr 12 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.38
- Generate tests summary after running tests.

* Thu Apr 11 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.37
- Rebuild to include latest deps.

* Tue Apr 9 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.36
- Remove dependencies to httpclient v3 from pom files.
- Resolved build problems caused by upstream changes.

* Mon Apr 8 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.35
- Add missing files to the commit.

* Mon Apr 8 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.34
- Fix the source build errors.

* Mon Apr 8 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.33
- Rebuild with ecf not requring commons logging 1.1.1.

* Mon Apr 8 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.32
- Drop dependency to ecf httpclient v3.
- Rebuild with new version of ecf.

* Mon Apr 8 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.31
- Drop org.eclipse.releng.* from build.
- Drop p2 discovery tests from build.
- Fix running tests.

* Mon Apr 8 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.30
- Remove unused bootstrap flag.

* Thu Apr 4 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.29
- Install icons for sclized version.
- Update to latest upstream.

* Thu Mar 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.28.git38f1df9
- Properly symlink ant dependencies.

* Mon Mar 18 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.27.git38f1df9
- Build against jetty 8 in sclized version.

* Mon Mar 18 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.26.git38f1df9
- RHBZ#902842 calls mvn-rpmbuild with -Dmaven.local.mode=true

* Thu Mar 14 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.25.git38f1df9
- Update to latest upstream.

* Tue Mar 5 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.24.git3fd9eca
- Add depmap for org.eclipse.jetty.orbit
- Resolves: rhbz#917619

* Tue Mar 5 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.23.git3fd9eca
- Add BR/R to tomcat-el-2.2-api.

* Fri Mar 1 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.22.git3fd9eca
- Use org.w3c.dom version provided by JVM in all ui bundles.

* Thu Feb 28 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.21.git3fd9eca
- Enable support for jetty 9.
- Improve the swt symlink to work well when sclized.

* Wed Feb 27 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.20.git3fd9eca
- Remove easymock and junit duplications from tests.

* Wed Feb 27 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.19.git3fd9eca
- Fix the /usr/lib/java/swt.jar symlink.

* Wed Feb 27 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.18.git3fd9eca
- Add support for jetty 9 (still disabled).

* Fri Feb 22 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.17.git3fd9eca
- Add BR to  xml-maven-plugin.

* Wed Feb 20 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.16.git3fd9eca
- Update to latest upstream version.

* Wed Feb 20 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.15.git201301281400
- Use EMF features from eclipse-emf-core.

* Tue Feb 19 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.14.git201301281400
- Add missing patch.

* Tue Feb 19 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.13.git201301281400
- RHBZ#912664 - eclipse-swt should put swt.jar into /usr/lib/java even on 64 bit systems.
- RHBZ#903537 - [abrt] java-1.7.0-openjdk-1.7.0.9-2.3.4.fc18: gtk_widget_real_map (SIGABRT)

* Tue Feb 12 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.12.git201301281400
- Build support for GTK2 and GTK3 together.

* Tue Feb 12 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.11.git201301281400
- Ability to use sclized icu4j.

* Mon Feb 11 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.10.git201301281400
- Yet another rebuild with latest icu4j.

* Sun Feb 10 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.9.git201301281400
- Another rebuild with latest icu4j.

* Fri Feb 8 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.8.git201301281400
- Rebuild with latest icu4j.

* Fri Feb 8 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.7.git201301281400
- Do fix the scl_root macro redefinition.

* Thu Feb 7 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.6.git201301281400
- Fix the scl_root macro.

* Thu Feb 7 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.5.git201301281400
- Add BR to gtk3.

* Thu Feb 7 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.4.git201301281400
- Upload proper sources.
- Export GTK_VERSION=3.0 during build.

* Wed Feb 6 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.3.git201301281400
- SCLize the spec.
- Enable SWT GTK3 support.
- Fix SWT build with rawhide.

* Tue Feb 5 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.2.git201301281400
- Fixed the generated eclipse.ini
- Fixed the content of generated swt.jar.
- Use maven macro to track poms in %%files section.

* Thu Jan 31 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.3.0-0.1.git20121217
- Update to Kepler.

* Fri Jan 25 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.2-0.5.git20121217
- RHBZ#832053: Ship SWT and other native plugins as folders.

* Thu Jan 17 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.2-0.4.git20121217
- RHBZ#893774: file shipped twice in eclipse-platform and eclipse-equinox-osgi

* Sat Jan 5 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.2-0.3.git20121217
- Fix missing about files on arm and ppc.

* Wed Jan 2 2013 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.2-0.2.git20121217
- Enable bootstrap (for the purpose of arm build).
- Fix the launcher build for arm.
- Fix the s390 build issue.

* Fri Dec 21 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.2-0.1.git20121217
- Update to pre SR2.

* Fri Dec 14 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-22
- Enable javadoc build.

* Mon Nov 26 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-21
- Remove javax.xml removal patch declaration.

* Fri Nov 23 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-19
- Excluded ResolverState from JIT to fix arm build.

* Thu Nov 22 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-18
- Get rid off javax.xml.
- Fix building launcher on arm.
- Fix RHBZ #878210

* Mon Nov 12 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-17
- Don't package non-existing fragments on s390, s390x.
- Add BR to GConf-2-devel

* Thu Nov 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-16
- Added debug symbols to SWT.
- Restored the debug package.
- Removed the debug flag from the build.

* Wed Nov 7 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-15
- Simplify initial repo creation.

* Tue Nov 6 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-14
- Export missing java home.

* Mon Nov 5 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-13
- Reduce the memory available for Tycho build.
- Reduce the build time.
- Use the upstream help generation patch.

* Wed Oct 31 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-12
- Remove the reference to org.apache.jasper (replaced by glassfish)

* Wed Oct 31 2012 Alexander Kurtakov <akurtako@redhat.com> 1:4.2.1-11
- Small cleanups.
- Bump release to be bigger than F-18.

* Wed Oct 24 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-9
- Make the removal of the icon more error prone.

* Tue Oct 23 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-8
- Remove a hack for building executable.

* Tue Oct 23 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-7
- Add profiles in the equinox executable for ppc and arm.

* Mon Oct 22 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-6
- Moved launcher version change after secondary fragments creation.
- Created some directories when creating secondary fragments.

* Fri Oct 19 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-5
- Removed patch for droping user installed changes.
- Moved Provides:osgi(system.bundle) to eclipse-equinox-osgi subpackage.
- Removed platform dependency to eclipse-rcp.
- Fixed building of core.net on secondary arches.

* Fri Oct 19 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-4
- Use glassfish-jsp-api instead of tomcat-jsp-api.

* Fri Oct 5 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-3
- Bootstrap build.
- Support for secondary architectures.

* Tue Oct 2 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-2
- Bump emf version to 2.8.1.

* Mon Oct 1 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-1
- Rebuild with latest emf 2.8.1.

* Fri Sep 28 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-0.4
- 861037: Eclipse does not start in rawhide

* Thu Sep 20 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-0.3
- Remove build artifacts from P2 files.
- Fix native gnome-proxy build.

* Wed Sep 19 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-0.2
- Build the jdt.debug.launching internal jar.

* Wed Sep 19 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.1-0.1
- Update to SR1 RC4.

* Mon Sep 17 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-19
- Add BR/R tomcat-jsp-2.2-api tp platform.

* Mon Sep 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-18
- Explicit dependency to jdt in platform.

* Fri Sep 7 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-17
- Yet another version of the previous patch.

* Fri Sep 7 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-16
- Remove remaining mina-core dependency.

* Fri Sep 7 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-15
- Use existing software group.
- Add BR to eclipse-pde
- Removed dependency on tomcat6
- Removed BR GConf2-devel.
- Removed BR apache-sshd.
- Removed BR/R tomcat-lib.
- jetty BR/R transformed to osgi() style.
- Excluded org.eclipse.equinox.console.jaas from builds.

* Wed Sep 5 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-14
- Native network support added.
- Native filesystem support added.
- Added test package.
- Generated help contents.

* Fri Aug 24 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-12
- Fix eclipse-pdebuild script to have proper path to pde bundle.
- Ensure there are right R dependencies between subpackages.
- Overall spec improvements.
- Bug 820248 - Start using glassfish-jsp

* Thu Aug 23 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-11
- Symlink junit 4.
- Move additional, non-Eclipse sources back to eclipse-build.
- Make the patch for setting BREE smaller.
- Patch for the compatibility.registry updated.
- Introduce a macro for symlinking.
- Bug 851190 - eclipse CBI build does not Requires: icu4j-eclipse

* Wed Aug 22 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-10
- Fix Eclipse not picking anything from dropins folder.

* Tue Aug 21 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-9
- Adopt upstream CBI system.

* Tue Aug 14 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-8
- Symlink emf bundles.

* Tue Aug 14 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-7
- Reduce the emf-core dependency strength.

* Wed Aug  1 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:4.2.0-6
- Move maven fragments and pom files in appropriate subpackages

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-4
- Bug 839986 - eclipse-rcp: broken symlinks

* Fri Jul 6 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-3
- Improved patch for discovering changes after update.

* Thu Jul 5 2012 Alexander Kurtakov <akurtako@redhat.com> 1:4.2.0-2
- Fix compilation against lucene 3.x.

* Fri Jun 29 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-1
- Included patch for Eclipse bug 251167
- Recompiled all jsr14 bundles as 1.5
- Update to final Juno release.
- Removed the old pdebuild script warning.
- Created OSGI subpackage.
- Removed the necessity to delete ~/.eclipse after some updates.

* Mon Jun 18 2012 Sami Wagiaalla <swagiaal@redhat.com> 1:4.2.0-0.24.I201205031800
- Remove empty reconciler script.

* Fri Jun 15 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.23.I201205031800
- Workaround for Eclipse bug 382574

* Thu May 24 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.22.I201205031800
- Do not pass the -preventMasterLaunch to non SDK applications.

* Fri May 18 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.21.I201205031800
- Prevent running Eclipse as root.
- Populate Update Sites.
- Pick renamed plugins on startup.
- Bundle the .option file for investigating startup problems.

* Sat May 5 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.20.I201205031800
- Update to M7.

* Mon Apr 30 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.19.I201204291800
- Update to I20120429-1800.

* Tue Apr 24 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.18.I201204171000
- Regenerating s390 and s390x launcher fragments from scratch.

* Mon Apr 23 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.17.I201204171000
- Remove duplicated junit library.
- Initial s390 and s390x support.
- Update to latest eclipse-build.

* Fri Apr 20 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.16.I201204171000
- Bug 814332 - Documentation is not pointing to locally installed javadoc.

* Thu Apr 19 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.15.I201204171000
- Amendment to previous release.

* Thu Apr 19 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.14.I201204171000
- Bug 813763 - /usr/bin/efj has missising exec permissions
- Bug 813756 - eclipse-jdt: bundled junit library
- Move hamcrest dependency to JDT.

* Wed Apr 18 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.13.I201204171000
- Move to the latest upstream I-build
- Generate full documentation.
- Formalize requirement on geronimo.

* Wed Apr 18 2012 Sami Wagiaalla <swagiaal@redhat.com> 1:4.2.0-0.12.I201204051114
- Don't fail if icon.xpm does not exist.

* Thu Apr 12 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.11.I201204051114
- Version more requirements.
- Move java requirement to the lowest-in-stack package.
- Removed some rpmlint warnings from spec file.

* Wed Apr 11 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.10.I201204051114
- Specified version for java-javadoc requirements.

* Tue Apr 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.9.I201204051114
- Add proper version to conflicts eclipse-emf-core

* Tue Apr 10 2012 Andrew Overholt <overholt@redhat.com> 1:4.2.0-0.8.I201204051114
- Add epoch to java and java-devel {Build,}Requires.

* Tue Apr 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.7.I201204051114
- Bug 810568 - require Java 7 to run.
- Bug 810970 - Cannot start 4.2.0-0.6.I201204051114.fc18.x86_64

* Fri Apr 6 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.6.I201204051114
- Update to I20120405-1114 upstream Eclipse build.
- Update to latest e-b
- Bug 810552 - JSch Requires should be versioned

* Wed Apr 4 2012 Roland Grunberg <rgrunber@redhat.com> 1:4.2.0-0.5.fa15ab
- Define %%{_eclipse_base} to properly resolve %%{_libdir} for noarch.

* Mon Apr 2 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.4.fa15ab
- pdebuild script installed into %%{_bindir}

* Thu Mar 29 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.3.fa15ab
- Sort out problems with versions.

* Thu Mar 29 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.2.fa15ab
- Change eclipse-emf-core package version to 2.8

* Thu Mar 29 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:4.2.0-0.1.fa15ab
- Update to 4.2
- Added eclipse-emf-core package.

* Mon Mar 26 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:3.8.0-0.21.I201203201400
- Added Provides: osgi(system.bundle)  to rcp package.

* Thu Mar 22 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:3.8.0-0.20.I201203201400
- Update to I20120320-1400.
- Ant version changed to 1.8.3.
- ECF version changed to 3.5.5.
- Experimental ARM support.

* Fri Mar 16 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:3.8.0-0.19.I201203141800
- Update to I20120314-1800.
- Eclipse-build updated to head.
- Required Jsch version updated to include correct MANIFEST.MF

* Sun Mar 11 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:3.8.0-0.18.I201203060800
- Update to I20120228-0800.
- Properly build org.eclipse.jdt.launching from source.

* Wed Feb 29 2012 Andrew Overholt <overholt@redhat.com> 1:3.8.0-0.17.I201202280800
- Add macro for build ID to ease moving to new ones.

* Wed Feb 29 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:3.8.0-0.16.I201202280800
- Eclipse update to I20120228-0800

* Wed Feb 22 2012 Roland Grunberg <rgrunber@redhat.com> 1:3.8.0-0.15.I201202140800
- Add org.eclipse.tycho:org.eclipse.osgi to osgi depmap.
- Install org.eclipse.jdt.core in javadir/eclipse.
- Add maven pom and depmap for org.eclipse.jdt.core.

* Wed Feb 22 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:3.8.0-0.14.I201202140800
- Updated dependencies to match jetty 8.1.0-1.
- Updated commons-codec minimal requirements.
- Moved icu4j dependency from swt to rcp.

* Fri Feb 17 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:3.8.0-0.13.I201202140800
- Add the icu4j-source bundle.
- Update to Eclipse build I20120214-0800.

* Thu Feb 16 2012 Sami Wagiaalla <swagiaal@redhat.com> 1:3.8.0-0.12.I201202070800
- Install a blank eclipse-reconciler.sh.

* Thu Feb 16 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:3.8.0-0.11.I201202070800
- Using system jar for junit 4 and different OSGI metadata for junit 3
- Adopt noarch icu4j-eclipse

* Mon Feb 13 2012 Sami Wagiaalla <swagiaal@redhat.com> 1:3.8.0-0.10.I201202070800
- Remove reconciler macros from macros.eclipse.
- Do not create temp eclipse directory in rpm-state.
- Do not install .so extaction paterns file.
- Stop running the reconciler.

* Thu Feb 9 2012 Sami Wagiaalla <swagiaal@redhat.com> 1:3.8.0-0.9.I201202070800
- Remove -debug reconciler flag
- Remove macro _eclipse_reqs.
- Define %%{_eclipse_base} in macros.eclipse.
- Pass dropins dir to reconciler when updating the platform.

* Wed Feb 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:3.8.0-0.7.I201201310842
- Drop the indirect dependency to tomcat 5.
- Support for gnomelibproxy on x86_64.

* Fri Feb 3 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:3.8.0-0.6.I201201310842
- Change the makefile patch to be truly universal

* Wed Feb 1 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:3.8.0-0.5.I201201310842
- Update to Eclipse 3.8 I20120131-0842

* Tue Jan 31 2012 Sami Wagiaalla <swagiaal@redhat.com> 1:3.8.0-0.4.I201201230800
- Remove xulrunner requirement.

* Tue Jan 31 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:3.8.0-0.3.I201201230800
- Updated dependency to felix-gogo-shell to include fix for bug 786041.
- Fixed mixed-use-of-spaces-and-tabs warning in the spec file.

* Tue Jan 31 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:3.8.0-0.2.I201201230800
- Version changed to a better format.

* Mon Jan 30 2012 Krzysztof Daniel <kdaniel@redhat.com> 1:3.8.0-0.M4c
- Update to Eclipse 3.8 I20120123-0800

* Fri Jan 20 2012 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.1-16
- Remove ORBit-2 requirement.

* Thu Jan 19 2012 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.1-15
- Add BuildRequires:  ORBit2-devel

* Thu Jan 19 2012 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.1-15
- Use rpm-state/eclipse for run-reconciler file instead of /var/run.
- Delete eclipse-tmpfiles.conf.

* Thu Jan 19 2012 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.1-14
- Remove _eclipse_pkg macro.
- Use mktemp for creating a backup directory in eclipse-reconciler.sh

* Mon Jan 16 2012 Alexander Kurtakov <akurtako@redhat.com> - 1:3.7.1-13
- Fix o.e.osgi.services pom to remove fake parent.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Andrew Overholt <overholt@redhat.com> 1:3.7.1-11
- Install org.eclipse.osgi.services and org.eclipse.equinox.http.servlet in
  javadir/eclipse.
- Add maven pom and depmap for the above.
- Fixes rhbz#769621.

* Tue Dec 20 2011 Andrew Robinson <arobinso@redhat.com> 1:3.7.1-10
- Specfile fix for license feature.

* Mon Dec 19 2011 Andrew Overholt <overholt@redhat.com> 1:3.7.1-9
- New eclipse-build snapshot with proper p2 repo URLs.

* Tue Nov 29 2011 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.1-8
- Stop using -clean option.
- Use -Dosgi.checkConfiguration=true when updating the platform.
- Remove cache.timestamps and .bundledata* when running the reconciler
  with -Dosgi.checkConfiguration=true.
- Do not verify %%{_libdir}/%%{name}/artifacts.xml.

* Tue Nov 29 2011 Roland Grunberg <rgrunber@redhat.com> 1:3.7.1-7
- Bump release.

* Fri Nov 25 2011 Alexander Kurtakov <akurtako@redhat.com> 1:3.7.1-6
- Add ExclusiveArch for RHEL.

* Fri Nov 25 2011 Roland Grunberg <rgrunber@redhat.com> 1:3.7.1-5
- (Re-apply) Upgrade to Tomcat 7 Jasper.
- Include org.eclipse.jdt.core as part of platform to avoid cyclic
  dependency between platform and jdt.

* Mon Nov 21 2011 Roland Grunberg <rgrunber@redhat.com> 1:3.7.1-4
- Bump release to match f16 branch.

* Wed Nov 16 2011 Roland Grunberg <rgrunber@redhat.com> 1:3.7.1-2
- Upload new source fixing RHBZ #753090.

* Tue Nov 08 2011 Roland Grunberg <rgrunber@redhat.com> 1:3.7.1-1
- Update to 3.7.1.
- org.apache.lucene no longer used upstream.

* Sat Oct 29 2011 Alexander Kurtakov <akurtako@redhat.com> 1:3.7.0-9
- New e-b snapshot - fixed Program.launch for remote uris.
- Adds _javadir/icu4j.jar for secondary archs bootstrapping.

* Wed Oct 26 2011 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.0-8
- Add Requires(post/postun) to _eclipse_pkg macro.

* Fri Oct 21 2011 Alexander Kurtakov <akurtako@redhat.com> 1:3.7.0-7
- Install org.eclipse.osgi in javadir/eclipse/osgi.jar
- Add maven pom and depmap.
- Fix compilation with glib 2.31.

* Thu Oct 20 2011 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.0-7
- Change _eclipse_pkg to pipe all reconciler output to /dev/null

* Thu Oct 20 2011 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.0-6
- Bump the release number.

* Wed Oct 19 2011 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.0-5
- Add new line before writing to eclipse.ini.

* Fri Oct 14 2011 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.0-5
- Change eclipse-reconciler script to run with no arguments.
- Use initscripts to create run directory.
- Run reconciler only once per install transaction.

* Tue Oct 4 2011 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.0-5
- New eclipse-build source tar ball.

* Mon Oct 3 2011 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.0-5
- Bump the relese number.

* Mon Oct 3 2011 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.0-5
- Remove all metadata files created by the reconciler before
  uninstallation.

* Mon Oct 3 2011 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.0-5
- Install .so extraction file.
- Extract .so files when the reconciler is run with -clean

* Mon Oct 3 2011 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.0-5
- Correct verification for files edited by the reconciler.
- Do not install state files.

* Mon Oct 3 2011 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.0-5
- Add Requires post and postun platform to jdt and pde on

* Fri Sep 23 2011 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.0-4
- Run reconciler after and before pde installation.

* Fri Sep 23 2011 Sami Wagiaalla <swagiaal@redhat.com> 1:3.7.0-4
- Add new script eclipse-reconciler.sh
- Run eclipse-reconciler.sh in the post and postun sections of jdt
  and post seciton on platform.
- Remove all old profiles in %%pre rcp.

* Wed Sep 21 2011 Alexander Kurtakov <akurtako@redhat.com> 1:3.7.0-4
- Remove _bindir/efj in pre - Fixes #738677.

* Mon Sep 12 2011 Alexander Kurtakov <akurtako@redhat.com> 1:3.7.0-3
- Use latest eclipse-build snapshot - fixes openjdk 7 build.
- Fix efj launcher script.

* Mon Jun 27 2011 Chris Aniszczyk <zx@redhat.com> 1:3.7.0-1.3
- Fix eclipse archive name

* Fri Jun 24 2011 Andrew Overholt <overholt@redhat.com> 1:3.7.0-1.2
- Fix SWT symlink in %%{_libdir} (rhbz#715470)

* Sun Jun 19 2011 Chris Aniszczyk <zx@redhat.com> 1:3.7.0-1.1
- Fix upload of e-b snapshot

* Wed Jun 15 2011 Chris Aniszczyk <zx@redhat.com> 1:3.7.0-1.0
- New e-b snapshot to update build on 3.7 Final

* Tue Jun 07 2011 Chris Aniszczyk <zx@redhat.com> 1:3.7.0-0.4.RC4
- New e-b snapshot to update build on 3.7 RC4
- Added usage of features back

* Thu Jun 02 2011 Chris Aniszczyk <zx@redhat.com> 1:3.7.0-0.3.RC3
- New e-b snapshot to update build on 3.7 RC3
- removed efj as it's part of eclipse-build now
- removed usage of features

* Tue May 17 2011 Chris Aniszczyk <zx@redhat.com> 1:3.7.0-0.2.RC1
- New e-b snapshot, fixes org.eclipse.equinox.util issue
- updated servlet and jsp related dependencies

* Tue May 17 2011 Chris Aniszczyk <zx@redhat.com> 1:3.7.0-0.1.RC1
- New e-b snapshot - first eclipse 3.7 build based on 3.7 RC1.

* Wed Apr 27 2011 Chris Aniszczyk <zx@redhat.com> 1:3.6.2-5
- New e-b snapshot - really fixes dropins issue.
- update sat4j dependency to 2.3.0

* Mon Apr 25 2011 Chris Aniszczyk <zx@redhat.com> 1:3.6.2-4
- Add rsync to BuildRequires.

* Mon Apr 25 2011 Chris Aniszczyk <zx@redhat.com> 1:3.6.2-3
- New e-b snapshot - fixes dropins issue.

* Fri Apr 8 2011 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.2-2
- New e-b snapshot - fixes Program.launch problem without libswt-gnome.

* Fri Apr 8 2011 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.2-1
- Switch to webkit by default.
- New eclipse-build snapshot.

* Wed Apr 6 2011 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.2-0.2
- Drop bootstrap conditional.
- Drop shell start script.
- Drop jpp versioned dependencies - apache-commons-* have never had such versions.
- Removed patches moved to eclipse-build.

* Fri Mar 11 2011 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.2-0.1
- First take on 3.6.2.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 3 2011 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.1-4
- Fix build with ant 1.8.2.

* Mon Dec 13 2010 Severin Gehwolf <sgehwolf@redhat.com> 1:3.6.1-3
- Add fix for Eclipse help XSS vulnerability (RH Bz #661901).

* Tue Oct 12 2010 Severin Gehwolf <sgehwolf@redhat.com> 1:3.6.1-2
- Require zip for eclipse-pde.

* Tue Oct 5 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.1-1
- Update to 3.6.1.

* Fri Oct 1 2010 Severin Gehwolf <sgehwolf@redhat.com> 1:3.6.0-17
- Push release #, since there has been a 3.6.0-16 scratch build.

* Thu Sep 30 2010 Severin Gehwolf <sgehwolf@redhat.com> 1:3.6.0-16
- Fix copy-platform script generation.

* Mon Sep 27 2010 Severin Gehwolf <sgehwolf@redhat.com> 1:3.6.0-15
- Add shell script portability patch for prepare-build-dir.sh.

* Tue Sep 21 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.0-14
- Really reenable webkit.

* Tue Sep 21 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.0-13
- Reenable webkit support, build is fixed.

* Tue Sep 21 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.0-12
- Disable webkit support - it is causing build failures.

* Tue Sep 21 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.0-11
- Add jsp-api dependency and use the tomcat6 one.

* Fri Sep 17 2010 Jeff Johnston <jjohnstn@redhat.com> 1:3.6.0-10
- Add patch to fix xpcom problem.

* Tue Sep 7 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.0-9
- Add webkitgtk-devel BR and webkit R.

* Wed Sep 1 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.0-8
- Add patch to remove ant-trax from ant bundle's classpath.
- Use new package names in BR/R.

* Wed Sep 1 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.0-7
- Update to eclipse-build 0.6.1 release.
- Fix build with ant 1.8.1.

* Tue Aug 17 2010 Andrew Overholt <overholt@redhat.com> 1:3.6.0-6
- Update to eclipse-build 0.6.1RC2.
- List a few files that were missing but should be installed.
- Finally remove %%{_datadir}/%%{name}/{features,plugins} as nothing is
  installed in there and shouldn't be.
- Use new eclipse-build targets provision.sdk and installSDKinDropins.
- Remove filenamepatterns.txt as it's now part of eclipse-build.
- Update download URL.
- Remove unused patches.

* Tue Aug 10 2010 Andrew Overholt <overholt@redhat.com> 1:3.6.0-5
- Update to eclipse-build 0.6.0 final.

* Fri Aug 06 2010 Andrew Overholt <overholt@redhat.com> 1:3.6.0-4
- Move epl-v10.html and notice.html to SWT sub-package.

* Thu Jul 15 2010 Elliott Baron <ebaron@fedoraproject.org> 1:3.6.0-3
- Increasing min versions for jetty, icu4j-eclipse and sat4j.

* Fri Jul 9 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.0-2
- o.e.core.net.linux is no longer x86 only.

* Fri Jul 9 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.0-1
- Update to 3.6.0.
- Based on eclipse-build 0.6.1 RC0.
