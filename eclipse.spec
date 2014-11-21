%{?_javapackages_macros:%_javapackages_macros}
%{?scl:%scl_package eclipse}
%{!?scl:%global pkg_name %{name}}
%{!?scl:%global _scl_root %{nil}}

# Set to 1 to build Eclipse without dependency to eclipse-pde
# Some parts (help) will not be built, and second run will be required,
# but this is a way to bootstrap Eclipse on secondary archs.
%global bootstrap       0


Epoch:                  1

%global eclipse_major   4
%global eclipse_minor   3
%global eclipse_majmin  %{eclipse_major}.%{eclipse_minor}
%global eclipse_micro   2
%global initialize      1
%global eb_commit       a9e58a88bc034454d79e896530be9b5b98f06dbe
%global eclipse_tag     R4_3_2
%global eclipse_version %{eclipse_majmin}.%{eclipse_micro}
%global installation_loc %{_libdir}/%{pkg_name}

%global _jetty_version 9.1.3
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
%ifarch s390 s390x ppc x86_64 aarch64
    %define eclipse_arch %{_arch}
%endif

# See fedora-devel-java-list discussion in September 2008.
#
# Prevent brp-java-repack-jars from being run.
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
Release:        4%{?dist}
License:        EPL
Group:          Development/Tools
URL:            http://www.eclipse.org/
#get-eclipse.sh
Source0:        R4_platform-aggregator-%{eclipse_tag}.tar.xz
Source1:        http://git.eclipse.org/c/linuxtools/org.eclipse.linuxtools.eclipse-build.git/snapshot/org.eclipse.linuxtools.eclipse-build-%{eb_commit}.tar.bz2

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
Patch2:         %{pkg_name}-no-source-for-dependencies.patch

# This has too many dependencies. We will not build it.
Patch3:         %{pkg_name}-remove-weaving.patch

# https://bugs.eclipse.org/bugs/show_bug.cgi?id=385970
Patch4:        %{pkg_name}-osgi-unpack-sources.patch

# https://bugs.eclipse.org/bugs/show_bug.cgi?id=379102
Patch5:        %{pkg_name}-do-not-run-as-root.patch

# https://bugs.eclipse.org/bugs/show_bug.cgi?id=377515
Patch6:        %{pkg_name}-p2-pick-up-renamed-jars.patch

# Patch for this was contributed. Unlikely to be released.
Patch7:        %{pkg_name}-ignore-version-when-calculating-home.patch

# CBI uses timestamps generated from the git commits. We don't have the repo,
# just source, and we don't want additional dependencies.
Patch8:        %{pkg_name}-remove-jgit-provider.patch

# This is for Fedora purposes to have working eclipse-pdebuild script.
Patch9:        %{pkg_name}-pdebuild-add-target.patch

# Strict Fedora purpose, too. We can't build entire product, just base
# and JDT and SDK as update sites, then we can assemble our own packages.
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=386670
# additional poms are a part of e-b
Patch10:        %{pkg_name}-change-build-packagings.patch

Patch11:        %{pkg_name}-test-support.patch

Patch12:        %{pkg_name}-secondary-arches.patch

Patch13:        %{pkg_name}-debug-symbols.patch

Patch14:        %{pkg_name}-fix-comaptibility-class.patch

Patch15:        %{pkg_name}-fix-swt-build-in-rawhide.patch

Patch16:        %{pkg_name}-bug-903537.patch

Patch17:        %{pkg_name}-jetty-9.patch

Patch18:        %{pkg_name}-fix-startup-class-refresh.patch

Patch19:        %{pkg_name}-fix-dropins.patch

Patch20:        %{pkg_name}-bug-408505.patch

Patch21:        %{pkg_name}-bug-386377.patch
Patch22:        %{pkg_name}-servlet-3.1.patch
Patch23:        %{pkg_name}-lucene-4.patch
Patch24:        %{pkg_name}-no-target-platform.patch

Patch101:	java8.patch

BuildRequires: ant >= 1.8.3
BuildRequires: rsync
%if 0%{?fedora}
BuildRequires: make, gcc
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: glib2-devel
%else
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(glib-2.0)
%endif
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
BuildRequires: lucene-core
BuildRequires: lucene-analysis
BuildRequires: junit >= 4.10-5
BuildRequires: hamcrest >= 0:1.1-11
BuildRequires: %{?scl_prefix}sat4j >= 2.3.5-1
BuildRequires: objectweb-asm3 >= 3.3.1-1
BuildRequires: zip
BuildRequires: sac >= 1.3-12
BuildRequires: batik  >= 1.8
BuildRequires: xml-commons-apis >= 1.4.01-12
BuildRequires: atinject >= 1-6
BuildRequires: tycho >= 0.16
BuildRequires: tycho-extras >= 0.16
BuildRequires: eclipse-emf-core >= 1:2.9.1-1
BuildRequires: %{?scl_prefix}eclipse-ecf-core >= 3.6.0-2
BuildRequires: tomcat-servlet-3.0-api
BuildRequires: tomcat-el-2.2-api
BuildRequires: glassfish-el
BuildRequires: glassfish-jsp-api >= 2.2.1-4
BuildRequires: glassfish-el-api
BuildRequires: cglib
BuildRequires: glassfish-jsp >= 2.2.5
BuildRequires: glassfish-servlet-api >= 3.1.0
BuildRequires: cbi-plugins
BuildRequires: xml-maven-plugin
BuildRequires: mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires: maven-deploy-plugin
BuildRequires: httpcomponents-core
BuildRequires: httpcomponents-client
%if ! %{bootstrap}
BuildRequires: eclipse-pde
%endif
BuildRequires: eclipse-license

%description
The Eclipse platform is designed for building integrated development
environments (IDEs), server-side applications, desktop applications, and
everything in between.

%package     swt
Summary:        SWT Library for GTK+
Group:          Development/Tools
# %%{_libdir}/java directory owned by jpackage-utils
Requires:       java >= 1:1.7.0
Requires:       jpackage-utils
Requires:       gtk2
Requires:       gtk+3.0
Requires:       webkit
Requires:       webkit3

%description swt
SWT Library for GTK+.

%package      equinox-osgi
Summary:        Eclipse OSGi - Equinox
Requires:       java-headless >= 1:1.7.0
Requires:       javapackages-tools
Provides:       osgi(system.bundle) = %{epoch}:%{eclipse_version}

%description  equinox-osgi
Eclipse OSGi - Equinox

%package        platform
Summary:        Eclipse platform common files
Group:          Development/Tools
Requires: ant-antlr ant-apache-bcel ant-apache-log4j ant-apache-oro ant-apache-regexp ant-apache-resolver ant-commons-logging ant-apache-bsf ant-commons-net
Requires: ant-javamail ant-jdepend ant-junit ant-swing ant-jsch ant-testutil ant-apache-xalan2 ant-jmf
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
Requires: lucene-core
Requires: lucene-analysis
Requires: %{?scl_prefix}sat4j >= 2.3.5-1
Requires: sac >= 1.3-12
Requires: xml-commons-apis >= 1.4.01-12
Requires: batik >= 1.8
Requires: atinject >= 1-6
Requires: geronimo-annotation >= 1.0-7
Requires: %{?scl_prefix}eclipse-ecf-core >= 3.6.0-2
Requires: eclipse-emf-core >= 2.9.1-1
Requires: tomcat-servlet-3.0-api
Requires: tomcat-el-2.2-api
Requires: glassfish-jsp-api >= 2.2.1-4
Requires: glassfish-jsp >= 2.2.5
Requires: glassfish-servlet-api >= 3.1.0
Requires: %{?scl_prefix}icu4j-eclipse >= 1:50.1.1
Requires: %{name}-swt = %{epoch}:%{eclipse_version}-%{release}
Requires: %{name}-equinox-osgi = %{epoch}:%{eclipse_version}-%{release}
Requires: httpcomponents-core
Requires: httpcomponents-client
%{?scl:Requires: %scl_runtime}
Obsoletes: %{name}-rcp < 1:4.3.0
Provides: %{name}-rcp = 1:%{eclipse_version}-%{release}

%description    platform
The Eclipse Platform is the base of all IDE plugins.  This does not include the
Java Development Tools or the Plugin Development Environment.

%package        jdt
Summary:        Eclipse Java Development Tools
Group:          Development/Tools
Requires:       %{name}-platform = %{epoch}:%{eclipse_version}-%{release}
Requires:       junit >= 4.10-5
Requires:       hamcrest >= 0:1.1-11

%description    jdt
Eclipse Java Development Tools.  This package is required to use Eclipse for
developing software written in the Java programming language.

%package        pde
Summary:        Eclipse Plugin Development Environment
Group:          Development/Tools
Provides:       %{name} = %{epoch}:%{eclipse_version}-%{release}
Requires:       %{name}-platform = %{epoch}:%{eclipse_version}-%{release}
Requires:       %{name}-jdt = %{epoch}:%{eclipse_version}-%{release}
Requires:       objectweb-asm3 >= 3.3.1-1
# For PDE Build wrapper script + creating jars
Requires:       zip
Requires:       bash

%description    pde
Eclipse Plugin Development Environment.  This package is required for
developing Eclipse plugins.

%package        tests
Summary:        Eclipse Tests
Group:          Development/Tools
Requires:       %{name}-pde = %{epoch}:%{eclipse_version}-%{release}
Requires:       %{?scl_prefix}easymock3

%description    tests
Eclipse Tests.

%prep

%setup -q %{SOURCE0} -n R4_platform-aggregator-%{eclipse_tag}

tar --strip-components=1 -xf %{SOURCE1} 

%patch0 -p1
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9
%patch10
%patch11
%patch12 -p1
%patch13
%patch14
%patch15
%patch16
%{!?scl:%patch17}
%patch18
%patch19
%patch20
pushd rt.equinox.framework
%patch21 -p1
popd
%patch22
%patch23 -p1
%patch24

%patch101

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

%pom_disable_module org.eclipse.ua.tests eclipse.platform.ua


#This part generates secondary fragments using primary fragments.
pushd  eclipse.platform.swt.binaries/bundles
    %_secondary gtk.linux.x86 x86 arm
    %_secondary gtk.linux.x86_64 x86_64 aarch64
    find . -name build.xml -exec sed -i -e "s/make_xulrunner//g" {} \;
    find . -name build.xml -exec sed -i -e "s/make_mozilla//g" {} \;
    find . -name build.xml -exec sed -i -e "s/make_xpcominit//g" {} \;
popd 
pushd eclipse.platform.resources/bundles
    %_secondary linux.x86 x86 arm
    %_secondary linux.x86 x86 s390
    %_secondary linux.x86_64 x86_64 s390x
    %_secondary linux.x86_64 x86_64 aarch64
popd
pushd eclipse.platform.team/bundles/org.eclipse.core.net/fragments
    %_secondary linux.x86 x86 arm
    %_secondary linux.x86 x86 ppc
    %_secondary linux.x86_64 x86_64 ppc64
    %_secondary linux.x86 x86 s390
    %_secondary linux.x86_64 x86_64 s390x
    %_secondary linux.x86_64 x86_64 aarch64
popd
pushd rt.equinox.framework/bundles
    %_secondary gtk.linux.x86 x86 arm
    %_secondary gtk.linux.x86_64 x86_64 aarch64
popd
pushd rt.equinox.binaries
    %_secondary gtk.linux.x86 x86 arm
    %_secondary gtk.linux.x86_64 x86_64 aarch64
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

cp -r /usr/share/java/eclipse-license/eclipse/features/* .m2/p2/repo-sdk/features
cp -r /usr/share/java/emf/eclipse/features/* .m2/p2/repo-sdk/features/
%{?scl: cp %{_javadir}/ecf/eclipse/plugins/* .m2/p2/repo-sdk/plugins}
%{?scl: cp %{_javadir}/*sat4j* .m2/p2/repo-sdk/plugins}
%if ! %{bootstrap}
cp -rf %{_libdir}/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_* .m2/p2/repo-sdk/plugins/
cp -rf %{_libdir}/eclipse/dropins/sdk/plugins/org.eclipse.pde.core_* .m2/p2/repo-sdk/plugins/
%else
# Use org.eclipse.tycho:org.eclipse.jdt.core (ecj)
sed -i -e 's@>org.eclipse.jdt<@>org.eclipse.tycho<@' eclipse-platform-parent/pom.xml
%endif

# Bump batik from 1.6.0 to 1.7.0
sed -i '/org\.apache\.batik/ s/1\.7\.0/1\.8\.0/' eclipse.platform.ui/bundles/org.eclipse.e4.ui.css.core/META-INF/MANIFEST.MF
sed -i 's/1\.6\.0/1\.7\.0/' eclipse.platform.ui/features/org.eclipse.e4.rcp/feature.xml

# Allow usage of javax.servlet.jsp 2.3.
sed -i '/javax\.servlet\.jsp/ s/2\.3/2\.4/' rt.equinox.bundles/bundles/org.eclipse.equinox.jsp.jasper/META-INF/MANIFEST.MF

# Use com.sun.el.java.el (Glassfish) instead of javax.el (Tomcat)
#sed -i 's/javax\.el/com\.sun\.el\.javax\.el/' eclipse.platform.releng/features/org.eclipse.help-feature/feature.xml

# Bump javax.servlet Import-Package statements
sed -i '/javax\.servlet/ s/3\.1/3\.2/' rt.equinox.bundles/bundles/org.eclipse.equinox.http.servlet/META-INF/MANIFEST.MF
sed -i '/javax\.servlet/ s/3\.1/3\.2/' rt.equinox.bundles/bundles/org.eclipse.equinox.jsp.jasper/META-INF/MANIFEST.MF

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
export MAVEN_OPTS="-Xmx1000m -XX:MaxPermSize=256m -XX:CompileCommand=exclude,org/eclipse/tycho/core/osgitools/EquinoxResolver,newState ${MAVEN_OPTS}"
export JAVA_HOME=%{java_home}


%if ! %{bootstrap}
pushd eclipse.platform.swt.binaries/bundles/org.eclipse.swt.gtk.linux.%{eclipse_arch}
    xmvn -o clean verify \
    -Dmaven.test.skip=true -Dnative=gtk.linux.%{eclipse_arch} \
    -Dtycho.local.keepTarget -Dmaven.repo.local=../../../.m2
popd
%endif

export GTK_VERSION=3.0
xmvn -o clean verify -P update-branding-plugins \
%if %{bootstrap}
   -P !api-generation,!build-docs \
%endif
   -Dmaven.test.skip=true -Dnative=gtk.linux.%{eclipse_arch} \
   -Dtycho.local.keepTarget -DbuildId=`echo "%{release}" | tr -d "."`

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

# This is a temporary hack
# We offer javax.servlet and javax.servlet-api as the same bundle
# References to javax.servlet should be renamed
pushd plugins
 f=`ls | grep -e "^javax.servlet-api_"`
 rm -f $f
 ln -s %{_javadir}/glassfish-servlet-api.jar $f
popd

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
 ln -s %{_javadir}/objectweb-asm3/asm-all.jar $f
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
%dir %{_libdir}/%{pkg_name}/configuration/org.eclipse.equinox.simpleconfigurator
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
%{_libdir}/%{pkg_name}/plugins/javax.servlet-api_*
%{_libdir}/%{pkg_name}/plugins/javax.servlet_*
%{_libdir}/%{pkg_name}/plugins/javax.servlet.jsp_*
%{_libdir}/%{pkg_name}/plugins/javax.xml_*
%{_libdir}/%{pkg_name}/plugins/javax.el_*
%{_libdir}/%{pkg_name}/plugins/javax.inject_*.jar
%{_libdir}/%{pkg_name}/plugins/glassfish-el.jar
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
* Wed Mar 19 2014 Mat Booth <fedora@matbooth.co.uk> - 1:4.3.2-3
- Accomodate for recent lucene package split.

* Tue Mar 18 2014 Mat Booth <fedora@matbooth.co.uk> - 1:4.3.2-2
- Rebuild p2 metadata.

* Wed Mar 12 2014 Mat Booth <fedora@matbooth.co.uk> - 1:4.3.2-1
- Update to 4.3.2

* Wed Mar 12 2014 Roland Grunberg <rgrunber@redhat.com> - 1:4.3.1-25
- Non bootstrap build.

* Mon Mar 10 2014 Roland Grunberg <rgrunber@redhat.com> - 1:4.3.1-24.2
- Fix API issues with Lucene 4.
- Remove old Tomcat Servlet API bundle.
- Use Glassfish EL instead of Tomcat EL.

* Thu Mar 06 2014 Roland Grunberg <rgrunber@redhat.com> - 1:4.3.1-24.1
- Update to Lucene 4.
- Update to Glassfish JSP 2.3.
- Enable bootstrap build to work around broken UA (Help) bundles.

* Thu Mar 6 2014 Alexander Kurtakov <akurtako@redhat.com> 1:4.3.1-24
- New e-b snapshot adapted to lucene changes.

* Tue Mar 04 2014 Michael Simacek <msimacek@redhat.com> - 1:4.3.1-23
- Rebuild for new jetty and httpcomponents-client

* Mon Mar 3 2014 Alexander Kurtakov <akurtako@redhat.com> 1:4.3.1-22
- Rebuild for new jetty.

* Wed Feb 26 2014 Alexander Kurtakov <akurtako@redhat.com> 1:4.3.1-21
- Non bootstrap build.

* Tue Feb 25 2014 Alexander Kurtakov <akurtako@redhat.com> 1:4.3.1-20.1
- Use new e-b snapshot that is adapted to ant packaging changes.
- Enable bootstrap build to work around broken runtime Eclipse.
- Make changes to deal with batik update (1.6.0 to 1.7.0).

* Fri Feb 21 2014 Alexander Kurtakov <akurtako@redhat.com> 1:4.3.1-20
- Require java-headless in equinox-osgi.

* Mon Feb 17 2014 Alexander Kurtakov <akurtako@redhat.com> 1:4.3.1-19
- Rebuild for new Jetty version.

* Thu Jan 30 2014 Sami Wagiaalla <swagiaal@redhat.com> - 1:4.3.1-18
- Increase JVM stack size for Maven. Fixes bz 1059816.

* Fri Jan 24 2014 Roland Grunberg <rgrunber@redhat.com> - 1:4.3.1-18
- Re-introduce and update bootstrapping capability.
- Add support for aarch64.

* Fri Jan 17 2014 Alexander Kurtakov <akurtako@redhat.com> 1:4.3.1-17
- Rebuild for Jetty 9.1.1.

* Mon Jan 6 2014 Alexander Kurtakov <akurtako@redhat.com> 1:4.3.1-16
- Rebuild for glassfish-jsp update.
- Add patch implementing servlet 3.1 methods.
- Disable o.e.ua.tests due to servlet 3.1 incompatibilities.

* Mon Dec 16 2013 Roland Grunberg <rgrunber@redhat.com> - 1:4.3.1-15
- Minor specfile cleanup.
- Merge Jetty 9 & Jetty 9.1 patches.
- Remove BuildRequires on eclipse-{egit,jgit}.

* Fri Dec 13 2013 Alexander Kurtakov <akurtako@redhat.com> 1:4.3.1-14
- Reenable API generation.

* Thu Dec 12 2013 Roland Grunberg <rgrunber@redhat.com> - 1:4.3.1-13
- Rebuild against Jetty 9.1.0. (Bug 1036888)
- Temporarily disable API Generation.

* Wed Dec 4 2013 Alexander Kurtakov <akurtako@redhat.com> 1:4.3.1-12
- Move pre-kepler changelog to separate file.
- Fix rpmlint warnings.
- Drop old provides/obsoletes.
- Give up on linking javadoc against local java-javadoc.
- Adapt to objectweb-asm3 rename.

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
