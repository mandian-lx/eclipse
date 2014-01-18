
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		eclipse
Epoch:		1
Version:	4.3.1
Release:	11.1
License:	GPLv3+
Source0:	eclipse-platform-4.3.1-11.0-omv2014.0.x86_64.rpm
Source1:	eclipse-equinox-osgi-4.3.1-11.0-omv2014.0.x86_64.rpm
Source2:	eclipse-jdt-4.3.1-11.0-omv2014.0.x86_64.rpm
Source3:	eclipse-pde-4.3.1-11.0-omv2014.0.x86_64.rpm
Source4:	swt.jar

URL:		https://abf.rosalinux.ru/openmandriva/eclipse-debuginfo
BuildArch:	noarch
Summary:	eclipse bootstrap version
Requires:	javapackages-bootstrap
Provides:	eclipse-debuginfo = 1:4.3.1-11.1:2014.0

%description
eclipse bootstrap version.


#------------------------------------------------------------------------
%package	-n eclipse-swt
Epoch:		1
Version:	4.3.1
Release:	11.0
Summary:	eclipse-swt bootstrap version
Requires:	javapackages-bootstrap
Provides:       osgi(org.eclipse.swt) = 3.102.1

%description	-n eclipse-swt
eclipse-swt bootstrap version.

%files		-n eclipse-swt
/usr/lib/eclipse
/usr/lib/java/swt.jar

#------------------------------------------------------------------------
%package	-n eclipse-platform
Epoch:		1
Version:	4.3.1
Release:	11.0
Summary:	eclipse-platform bootstrap version
Requires:	javapackages-bootstrap
Requires:	ant-antlr
Requires:	ant-apache-bcel
Requires:	ant-apache-bsf
Requires:	ant-apache-log4j
Requires:	ant-apache-oro
Requires:	ant-apache-regexp
Requires:	ant-apache-resolver
Requires:	ant-apache-xalan2
Requires:	ant-commons-logging
Requires:	ant-commons-net
Requires:	ant-javamail
Requires:	ant-jdepend
Requires:	ant-jmf
Requires:	ant-jsch
Requires:	ant-junit
Requires:	ant-scripts
Requires:	ant-swing
Requires:	ant-testutil
Requires:	apache-commons-codec >= 1.6-2
Requires:	apache-commons-el >= 1.0-23
Requires:	apache-commons-logging
Requires:	atinject >= 1-6
Requires:	batik >= 1.8
Requires:	eclipse-ecf-core >= 3.6.0-2
Requires:	eclipse-emf-core >= 2.9.0-1
Requires:	eclipse-equinox-osgi = 1:4.3.1-11.0
Requires:	eclipse-swt = 1:4.3.1-11.1
Requires:	felix-gogo-command >= 0.12
Requires:	felix-gogo-shell >= 0.10.0-3
Requires:	geronimo-annotation >= 1.0-7
Requires:	glassfish-jsp >= 2.2.5
Requires:	glassfish-jsp-api >= 2.2.1-4
Requires:	httpcomponents-client
Requires:	httpcomponents-core
Requires:	icu4j-eclipse >= 1:50.1.1
Requires:	jpackage-utils
Requires:	jsch >= 0.1.46-2
Requires:	lucene >= 2.9.4-8
Requires:	lucene-contrib >= 2.9.4-8
Requires:	osgi(com.ibm.icu)
Requires:	osgi(com.jcraft.jsch)
Requires:	osgi(org.apache.batik.css)
Requires:	osgi(org.apache.lucene.analysis)
Requires:	osgi(org.apache.lucene.core)
Requires:	osgi(org.eclipse.ecf)
Requires:	osgi(org.eclipse.ecf.filetransfer)
Requires:	osgi(org.eclipse.ecf.provider.filetransfer)
Requires:	osgi(org.eclipse.emf.ecore)
Requires:	osgi(org.eclipse.emf.ecore.change)
Requires:	osgi(org.eclipse.emf.ecore.xmi)
Requires:	osgi(org.eclipse.jetty.continuation) >= 9
Requires:	osgi(org.eclipse.jetty.http) >= 9
Requires:	osgi(org.eclipse.jetty.io) >= 9
Requires:	osgi(org.eclipse.jetty.security) >= 9
Requires:	osgi(org.eclipse.jetty.server) >= 9
Requires:	osgi(org.eclipse.jetty.servlet) >= 9
Requires:	osgi(org.eclipse.jetty.util) >= 9
Requires:	osgi(org.eclipse.osgi)
Requires:	osgi(org.eclipse.osgi.services)
Requires:	osgi(org.eclipse.swt)
Requires:	osgi(org.sat4j.core)
Requires:	osgi(org.sat4j.pb)
Requires:	osgi(org.w3c.css.sac)
Requires:	sac >= 1.3-12
Requires:	sat4j >= 2.3.5-1
Requires:	tomcat-el-2.2-api
Requires:	tomcat-servlet-3.0-api
Requires:	xml-commons-apis >= 1.4.01-12
Provides:	eclipse-cvs-client = 1:4.3.1-11.1
Provides:	eclipse-platform = 1:4.3.1-11.1:2014.0
Provides:	eclipse-rcp = 1:4.3.1-11.1
Provides:	mvn(org.eclipse.equinox.http:servlet) = 1.0.0-v20070606
Provides:	osgi(org.apache.ant) = 1.8.4
Provides:	osgi(org.eclipse.ant.core) = 3.2.500
Provides:	osgi(org.eclipse.compare) = 3.5.401
Provides:	osgi(org.eclipse.compare.core) = 3.5.300
Provides:	osgi(org.eclipse.core.commands) = 3.6.100
Provides:	osgi(org.eclipse.core.contenttype) = 3.4.200
Provides:	osgi(org.eclipse.core.databinding) = 1.4.1
Provides:	osgi(org.eclipse.core.databinding.beans) = 1.2.200
Provides:	osgi(org.eclipse.core.databinding.observable) = 1.4.1
Provides:	osgi(org.eclipse.core.databinding.property) = 1.4.200
Provides:	osgi(org.eclipse.core.expressions) = 3.4.500
Provides:	osgi(org.eclipse.core.externaltools) = 1.0.200
Provides:	osgi(org.eclipse.core.filebuffers) = 3.5.300
Provides:	osgi(org.eclipse.core.filesystem) = 1.4.0
Provides:	osgi(org.eclipse.core.filesystem.linux.x86_64) = 1.2.100
Provides:	osgi(org.eclipse.core.jobs) = 3.5.300
Provides:	osgi(org.eclipse.core.net) = 1.2.200
Provides:	osgi(org.eclipse.core.net.linux.x86_64) = 1.1.100
Provides:	osgi(org.eclipse.core.resources) = 3.8.101
Provides:	osgi(org.eclipse.core.runtime) = 3.9.0
Provides:	osgi(org.eclipse.core.runtime.compatibility) = 3.2.200
Provides:	osgi(org.eclipse.core.runtime.compatibility.registry) = 3.5.200
Provides:	osgi(org.eclipse.core.variables) = 3.2.700
Provides:	osgi(org.eclipse.cvs) = 1.4.0
Provides:	osgi(org.eclipse.debug.core) = 3.8.0
Provides:	osgi(org.eclipse.debug.ui) = 3.9.0
Provides:	osgi(org.eclipse.e4.core.commands) = 0.10.2
Provides:	osgi(org.eclipse.e4.core.contexts) = 1.3.1
Provides:	osgi(org.eclipse.e4.core.di) = 1.3.0
Provides:	osgi(org.eclipse.e4.core.di.extensions) = 0.11.100
Provides:	osgi(org.eclipse.e4.core.services) = 1.1.0
Provides:	osgi(org.eclipse.e4.ui.bindings) = 0.10.101
Provides:	osgi(org.eclipse.e4.ui.css.core) = 0.10.100
Provides:	osgi(org.eclipse.e4.ui.css.swt) = 0.11.0
Provides:	osgi(org.eclipse.e4.ui.css.swt.theme) = 0.9.100
Provides:	osgi(org.eclipse.e4.ui.di) = 1.0.0
Provides:	osgi(org.eclipse.e4.ui.model.workbench) = 1.0.1
Provides:	osgi(org.eclipse.e4.ui.services) = 1.0.1
Provides:	osgi(org.eclipse.e4.ui.widgets) = 1.0.0
Provides:	osgi(org.eclipse.e4.ui.workbench) = 1.0.1
Provides:	osgi(org.eclipse.e4.ui.workbench.addons.swt) = 1.0.1
Provides:	osgi(org.eclipse.e4.ui.workbench.renderers.swt) = 0.11.1
Provides:	osgi(org.eclipse.e4.ui.workbench.swt) = 0.12.1
Provides:	osgi(org.eclipse.e4.ui.workbench3) = 0.12.0
Provides:	osgi(org.eclipse.equinox.app) = 1.3.100
Provides:	osgi(org.eclipse.equinox.bidi) = 0.10.0
Provides:	osgi(org.eclipse.equinox.common) = 3.6.200
Provides:	osgi(org.eclipse.equinox.concurrent) = 1.1.0
Provides:	osgi(org.eclipse.equinox.console) = 1.0.100
Provides:	osgi(org.eclipse.equinox.ds) = 1.4.101
Provides:	osgi(org.eclipse.equinox.event) = 1.3.0
Provides:	osgi(org.eclipse.equinox.frameworkadmin) = 2.0.100
Provides:	osgi(org.eclipse.equinox.frameworkadmin.equinox) = 1.0.500
Provides:	osgi(org.eclipse.equinox.http.jetty) = 3.0.100
Provides:	osgi(org.eclipse.equinox.http.registry) = 1.1.300
Provides:	osgi(org.eclipse.equinox.http.servlet) = 1.1.400
Provides:	osgi(org.eclipse.equinox.jsp.jasper) = 1.0.400
Provides:	osgi(org.eclipse.equinox.jsp.jasper.registry) = 1.0.300
Provides:	osgi(org.eclipse.equinox.launcher) = 1.3.0
Provides:	osgi(org.eclipse.equinox.launcher.gtk.linux.x86_64) = 1.1.200
Provides:	osgi(org.eclipse.equinox.p2.artifact.repository) = 1.1.200
Provides:	osgi(org.eclipse.equinox.p2.console) = 1.0.300
Provides:	osgi(org.eclipse.equinox.p2.core) = 2.3.0
Provides:	osgi(org.eclipse.equinox.p2.director) = 2.3.0
Provides:	osgi(org.eclipse.equinox.p2.director.app) = 1.0.300
Provides:	osgi(org.eclipse.equinox.p2.directorywatcher) = 1.0.300
Provides:	osgi(org.eclipse.equinox.p2.engine) = 2.3.0
Provides:	osgi(org.eclipse.equinox.p2.extensionlocation) = 1.2.100
Provides:	osgi(org.eclipse.equinox.p2.garbagecollector) = 1.0.200
Provides:	osgi(org.eclipse.equinox.p2.jarprocessor) = 1.0.300
Provides:	osgi(org.eclipse.equinox.p2.metadata) = 2.2.0
Provides:	osgi(org.eclipse.equinox.p2.metadata.repository) = 1.2.100
Provides:	osgi(org.eclipse.equinox.p2.operations) = 2.3.0
Provides:	osgi(org.eclipse.equinox.p2.publisher) = 1.3.0
Provides:	osgi(org.eclipse.equinox.p2.publisher.eclipse) = 1.1.200
Provides:	osgi(org.eclipse.equinox.p2.ql) = 2.0.100
Provides:	osgi(org.eclipse.equinox.p2.reconciler.dropins) = 1.1.200
Provides:	osgi(org.eclipse.equinox.p2.repository) = 2.3.0
Provides:	osgi(org.eclipse.equinox.p2.repository.tools) = 2.1.0
Provides:	osgi(org.eclipse.equinox.p2.touchpoint.eclipse) = 2.1.200
Provides:	osgi(org.eclipse.equinox.p2.touchpoint.natives) = 1.1.100
Provides:	osgi(org.eclipse.equinox.p2.transport.ecf) = 1.1.0
Provides:	osgi(org.eclipse.equinox.p2.ui) = 2.3.0
Provides:	osgi(org.eclipse.equinox.p2.ui.importexport) = 1.1.0
Provides:	osgi(org.eclipse.equinox.p2.ui.sdk) = 1.0.300
Provides:	osgi(org.eclipse.equinox.p2.ui.sdk.scheduler) = 1.2.0
Provides:	osgi(org.eclipse.equinox.p2.updatechecker) = 1.1.200
Provides:	osgi(org.eclipse.equinox.p2.updatesite) = 1.0.400
Provides:	osgi(org.eclipse.equinox.preferences) = 3.5.100
Provides:	osgi(org.eclipse.equinox.registry) = 3.5.301
Provides:	osgi(org.eclipse.equinox.security) = 1.2.0
Provides:	osgi(org.eclipse.equinox.security.ui) = 1.1.100
Provides:	osgi(org.eclipse.equinox.simpleconfigurator) = 1.0.400
Provides:	osgi(org.eclipse.equinox.simpleconfigurator.manipulator) = 2.0.0
Provides:	osgi(org.eclipse.equinox.util) = 1.0.500
Provides:	osgi(org.eclipse.help) = 3.6.0
Provides:	osgi(org.eclipse.help.base) = 4.0.0
Provides:	osgi(org.eclipse.help.ui) = 4.0.1
Provides:	osgi(org.eclipse.help.webapp) = 3.6.200
Provides:	osgi(org.eclipse.jdt.core) = 3.9.1
Provides:	osgi(org.eclipse.jface) = 3.9.1
Provides:	osgi(org.eclipse.jface.databinding) = 1.6.200
Provides:	osgi(org.eclipse.jface.text) = 3.8.101
Provides:	osgi(org.eclipse.jsch.core) = 1.1.400
Provides:	osgi(org.eclipse.jsch.ui) = 1.1.400
Provides:	osgi(org.eclipse.ltk.core.refactoring) = 3.6.100
Provides:	osgi(org.eclipse.ltk.ui.refactoring) = 3.7.100
Provides:	osgi(org.eclipse.platform) = 4.3.1
Provides:	osgi(org.eclipse.platform.doc.user) = 4.3.0
Provides:	osgi(org.eclipse.rcp) = 4.3.0
Provides:	osgi(org.eclipse.search) = 3.9.0
Provides:	osgi(org.eclipse.team.core) = 3.7.0
Provides:	osgi(org.eclipse.team.cvs.core) = 3.3.500
Provides:	osgi(org.eclipse.team.cvs.ssh2) = 3.2.300
Provides:	osgi(org.eclipse.team.cvs.ui) = 3.3.600
Provides:	osgi(org.eclipse.team.ui) = 3.7.1
Provides:	osgi(org.eclipse.text) = 3.5.300
Provides:	osgi(org.eclipse.ui) = 3.105.0
Provides:	osgi(org.eclipse.ui.browser) = 3.4.100
Provides:	osgi(org.eclipse.ui.cheatsheets) = 3.4.200
Provides:	osgi(org.eclipse.ui.console) = 3.5.200
Provides:	osgi(org.eclipse.ui.editors) = 3.8.100
Provides:	osgi(org.eclipse.ui.externaltools) = 3.2.200
Provides:	osgi(org.eclipse.ui.forms) = 3.6.1
Provides:	osgi(org.eclipse.ui.ide) = 3.9.1
Provides:	osgi(org.eclipse.ui.ide.application) = 1.0.400
Provides:	osgi(org.eclipse.ui.intro) = 3.4.200
Provides:	osgi(org.eclipse.ui.intro.universal) = 3.2.600
Provides:	osgi(org.eclipse.ui.navigator) = 3.5.300
Provides:	osgi(org.eclipse.ui.navigator.resources) = 3.4.500
Provides:	osgi(org.eclipse.ui.net) = 1.2.200
Provides:	osgi(org.eclipse.ui.views) = 3.6.100
Provides:	osgi(org.eclipse.ui.views.properties.tabbed) = 3.6.0
Provides:	osgi(org.eclipse.ui.workbench) = 3.105.1
Provides:	osgi(org.eclipse.ui.workbench.texteditor) = 3.8.101
Provides:	osgi(org.eclipse.update.configurator) = 3.3.200
Obsoletes:	eclipse-cvs-client < 1:3.3.2-20
Obsoletes:	eclipse-rcp < 1:4.3.0

%description	-n eclipse-platform
eclipse-platform bootstrap version.

%files		-n eclipse-platform
/etc/eclipse.ini
/usr/bin/eclipse
/usr/lib64/eclipse/.eclipseproduct
/usr/lib64/eclipse/about.html
/usr/lib64/eclipse/about_files
/usr/lib64/eclipse/about_files/IJG_README
/usr/lib64/eclipse/about_files/lgpl-v21.txt
/usr/lib64/eclipse/about_files/mpl-v11.txt
/usr/lib64/eclipse/about_files/webkit-bsd.txt
/usr/lib64/eclipse/artifacts.xml
/usr/lib64/eclipse/configuration
/usr/lib64/eclipse/configuration/config.ini
/usr/lib64/eclipse/configuration/org.eclipse.equinox.simpleconfigurator/bundles.info
/usr/lib64/eclipse/dropins
/usr/lib64/eclipse/eclipse
/usr/lib64/eclipse/eclipse.ini
/usr/lib64/eclipse/features
/usr/lib64/eclipse/features/org.eclipse.cvs_1.4.0.v20140117-1748
/usr/lib64/eclipse/features/org.eclipse.cvs_1.4.0.v20140117-1748/META-INF
/usr/lib64/eclipse/features/org.eclipse.cvs_1.4.0.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/features/org.eclipse.cvs_1.4.0.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/features/org.eclipse.cvs_1.4.0.v20140117-1748/feature.properties
/usr/lib64/eclipse/features/org.eclipse.cvs_1.4.0.v20140117-1748/feature.xml
/usr/lib64/eclipse/features/org.eclipse.cvs_1.4.0.v20140117-1748/license.html
/usr/lib64/eclipse/features/org.eclipse.e4.rcp_1.2.1.v20140117-1748
/usr/lib64/eclipse/features/org.eclipse.e4.rcp_1.2.1.v20140117-1748/META-INF
/usr/lib64/eclipse/features/org.eclipse.e4.rcp_1.2.1.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/features/org.eclipse.e4.rcp_1.2.1.v20140117-1748/eclipse_update_120.jpg
/usr/lib64/eclipse/features/org.eclipse.e4.rcp_1.2.1.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/features/org.eclipse.e4.rcp_1.2.1.v20140117-1748/feature.properties
/usr/lib64/eclipse/features/org.eclipse.e4.rcp_1.2.1.v20140117-1748/feature.xml
/usr/lib64/eclipse/features/org.eclipse.e4.rcp_1.2.1.v20140117-1748/license.html
/usr/lib64/eclipse/features/org.eclipse.emf.common_2.9.1.v20130930-0823
/usr/lib64/eclipse/features/org.eclipse.emf.common_2.9.1.v20130930-0823/epl-v10.html
/usr/lib64/eclipse/features/org.eclipse.emf.common_2.9.1.v20130930-0823/feature.properties
/usr/lib64/eclipse/features/org.eclipse.emf.common_2.9.1.v20130930-0823/feature.xml
/usr/lib64/eclipse/features/org.eclipse.emf.common_2.9.1.v20130930-0823/license.html
/usr/lib64/eclipse/features/org.eclipse.emf.ecore_2.9.1.v20130930-0823
/usr/lib64/eclipse/features/org.eclipse.emf.ecore_2.9.1.v20130930-0823/epl-v10.html
/usr/lib64/eclipse/features/org.eclipse.emf.ecore_2.9.1.v20130930-0823/feature.properties
/usr/lib64/eclipse/features/org.eclipse.emf.ecore_2.9.1.v20130930-0823/feature.xml
/usr/lib64/eclipse/features/org.eclipse.emf.ecore_2.9.1.v20130930-0823/license.html
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.core.feature_1.2.1.v20140117-1748
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.core.feature_1.2.1.v20140117-1748/META-INF
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.core.feature_1.2.1.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.core.feature_1.2.1.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.core.feature_1.2.1.v20140117-1748/feature.properties
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.core.feature_1.2.1.v20140117-1748/feature.xml
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.core.feature_1.2.1.v20140117-1748/license.html
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.extras.feature_1.2.0.v20140117-1748
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.extras.feature_1.2.0.v20140117-1748/META-INF
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.extras.feature_1.2.0.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.extras.feature_1.2.0.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.extras.feature_1.2.0.v20140117-1748/feature.properties
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.extras.feature_1.2.0.v20140117-1748/feature.xml
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.extras.feature_1.2.0.v20140117-1748/license.html
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.rcp.feature_1.2.0.v20140117-1748
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.rcp.feature_1.2.0.v20140117-1748/META-INF
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.rcp.feature_1.2.0.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.rcp.feature_1.2.0.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.rcp.feature_1.2.0.v20140117-1748/feature.properties
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.rcp.feature_1.2.0.v20140117-1748/feature.xml
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.rcp.feature_1.2.0.v20140117-1748/license.html
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.user.ui_2.2.0.v20140117-1748
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.user.ui_2.2.0.v20140117-1748/META-INF
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.user.ui_2.2.0.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.user.ui_2.2.0.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.user.ui_2.2.0.v20140117-1748/feature.properties
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.user.ui_2.2.0.v20140117-1748/feature.xml
/usr/lib64/eclipse/features/org.eclipse.equinox.p2.user.ui_2.2.0.v20140117-1748/license.html
/usr/lib64/eclipse/features/org.eclipse.help_2.0.1.v20140117-1748
/usr/lib64/eclipse/features/org.eclipse.help_2.0.1.v20140117-1748/META-INF
/usr/lib64/eclipse/features/org.eclipse.help_2.0.1.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/features/org.eclipse.help_2.0.1.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/features/org.eclipse.help_2.0.1.v20140117-1748/feature.properties
/usr/lib64/eclipse/features/org.eclipse.help_2.0.1.v20140117-1748/feature.xml
/usr/lib64/eclipse/features/org.eclipse.help_2.0.1.v20140117-1748/license.html
/usr/lib64/eclipse/features/org.eclipse.platform_4.3.1.v20140117-1748
/usr/lib64/eclipse/features/org.eclipse.platform_4.3.1.v20140117-1748/META-INF
/usr/lib64/eclipse/features/org.eclipse.platform_4.3.1.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/features/org.eclipse.platform_4.3.1.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/features/org.eclipse.platform_4.3.1.v20140117-1748/feature.properties
/usr/lib64/eclipse/features/org.eclipse.platform_4.3.1.v20140117-1748/feature.xml
/usr/lib64/eclipse/features/org.eclipse.platform_4.3.1.v20140117-1748/license.html
/usr/lib64/eclipse/features/org.eclipse.rcp.configuration_1.0.0.v20140117-1748
/usr/lib64/eclipse/features/org.eclipse.rcp.configuration_1.0.0.v20140117-1748/META-INF
/usr/lib64/eclipse/features/org.eclipse.rcp.configuration_1.0.0.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/features/org.eclipse.rcp.configuration_1.0.0.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/features/org.eclipse.rcp.configuration_1.0.0.v20140117-1748/feature.properties
/usr/lib64/eclipse/features/org.eclipse.rcp.configuration_1.0.0.v20140117-1748/feature.xml
/usr/lib64/eclipse/features/org.eclipse.rcp.configuration_1.0.0.v20140117-1748/license.html
/usr/lib64/eclipse/features/org.eclipse.rcp_4.3.1.v20140117-1748
/usr/lib64/eclipse/features/org.eclipse.rcp_4.3.1.v20140117-1748/META-INF
/usr/lib64/eclipse/features/org.eclipse.rcp_4.3.1.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/features/org.eclipse.rcp_4.3.1.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/features/org.eclipse.rcp_4.3.1.v20140117-1748/feature.properties
/usr/lib64/eclipse/features/org.eclipse.rcp_4.3.1.v20140117-1748/feature.xml
/usr/lib64/eclipse/features/org.eclipse.rcp_4.3.1.v20140117-1748/license.html
/usr/lib64/eclipse/p2
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.core
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.core/cache
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/.settings
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/.settings/org.eclipse.equinox.p2.artifact.repository.prefs
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/.settings/org.eclipse.equinox.p2.metadata.repository.prefs
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/SDKProfile.profile
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/SDKProfile.profile/.data
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/SDKProfile.profile/.data/.settings
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/SDKProfile.profile/.data/.settings/org.eclipse.equinox.p2.artifact.repository.prefs
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/SDKProfile.profile/.data/.settings/org.eclipse.equinox.p2.metadata.repository.prefs
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/SDKProfile.profile/.data/org.eclipse.equinox.internal.p2.touchpoint.eclipse.actions
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/SDKProfile.profile/.data/org.eclipse.equinox.internal.p2.touchpoint.eclipse.actions/jvmargs
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/SDKProfile.profile/.lock
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/SDKProfile.profile/1389984491424.profile.gz
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/SDKProfile.profile/1389984491431.profile.gz
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/SDKProfile.profile/1389984502133.profile.gz
/usr/lib64/eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/SDKProfile.profile/1389984502816.profile.gz
/usr/lib64/eclipse/plugins/com.ibm.icu_50.1.1.v20130412.jar
/usr/lib64/eclipse/plugins/com.jcraft.jsch_0.1.50.jar
/usr/lib64/eclipse/plugins/javax.el_2.2.0.jar
/usr/lib64/eclipse/plugins/javax.inject_1.0.0.v20091030.jar
/usr/lib64/eclipse/plugins/javax.servlet.jsp_2.2.1.jar
/usr/lib64/eclipse/plugins/javax.servlet_3.0.0.jar
/usr/lib64/eclipse/plugins/javax.xml_1.3.4.v201005080400.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/META-INF
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/META-INF/MANIFEST.MF
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/META-INF/eclipse.inf
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/about.html
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/about_files
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/about_files/ASL-LICENSE-2.0.txt
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/about_files/DOM-LICENSE.html
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/about_files/LICENSE
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/about_files/NOTICE
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/about_files/SAX-LICENSE.html
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/bin
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/bin/ant
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/bin/antRun
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/bin/antRun.pl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/bin/complete-and-cmd.pl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/bin/runant.pl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/bin/runant.py
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/ant-bootstrap.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/changelog.xsl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/checkstyle
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/checkstyle/checkstyle-frames.xsl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/checkstyle/checkstyle-text.xsl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/checkstyle/checkstyle-xdoc.xsl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/coverage-frames.xsl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/jdepend-frames.xsl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/jdepend.xsl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/junit-frames-xalan1.xsl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/junit-frames.xsl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/junit-noframes.xsl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/log.xsl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/maudit-frames.xsl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/mmetrics-frames.xsl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/etc/tagdiff.xsl
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-antlr.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-apache-bcel.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-apache-bsf.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-apache-log4j.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-apache-oro.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-apache-regexp.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-apache-resolver.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-apache-xalan2.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-commons-logging.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-commons-net.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-javamail.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-jdepend.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-jmf.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-jsch.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-junit.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-launcher.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-swing.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant-testutil.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/ant.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/lib/junit4.jar
/usr/lib64/eclipse/plugins/org.apache.ant_1.8.4.v201209061652/plugin.properties
/usr/lib64/eclipse/plugins/org.apache.batik.css_1.6.0.v201011041432.jar
/usr/lib64/eclipse/plugins/org.apache.batik.util.gui_1.6.0.v201011041432.jar
/usr/lib64/eclipse/plugins/org.apache.batik.util_1.6.0.v201011041432.jar
/usr/lib64/eclipse/plugins/org.apache.commons.codec_1.8.0.jar
/usr/lib64/eclipse/plugins/org.apache.commons.logging_1.1.3.jar
/usr/lib64/eclipse/plugins/org.apache.felix.gogo.command_0.12.0.jar
/usr/lib64/eclipse/plugins/org.apache.felix.gogo.runtime_0.10.0.jar
/usr/lib64/eclipse/plugins/org.apache.felix.gogo.shell_0.10.0.jar
/usr/lib64/eclipse/plugins/org.apache.geronimo.specs.geronimo-annotation_1.1_spec_1.0.0.jar
/usr/lib64/eclipse/plugins/org.apache.httpcomponents.httpclient_4.2.5.jar
/usr/lib64/eclipse/plugins/org.apache.httpcomponents.httpcore_4.2.4.jar
/usr/lib64/eclipse/plugins/org.apache.lucene.analysis_3.6.2.jar
/usr/lib64/eclipse/plugins/org.apache.lucene.core_3.6.2.jar
/usr/lib64/eclipse/plugins/org.eclipse.ant.core_3.2.500.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.compare.core_3.5.300.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.compare_3.5.401.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.commands_3.6.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.contenttype_3.4.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.databinding.beans_1.2.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.databinding.observable_1.4.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.databinding.property_1.4.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.databinding_1.4.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.expressions_3.4.500.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.externaltools_1.0.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.filebuffers_3.5.300.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.filesystem.linux.x86_64_1.2.100.v20140117-1748
/usr/lib64/eclipse/plugins/org.eclipse.core.filesystem.linux.x86_64_1.2.100.v20140117-1748/META-INF
/usr/lib64/eclipse/plugins/org.eclipse.core.filesystem.linux.x86_64_1.2.100.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/plugins/org.eclipse.core.filesystem.linux.x86_64_1.2.100.v20140117-1748/about.html
/usr/lib64/eclipse/plugins/org.eclipse.core.filesystem.linux.x86_64_1.2.100.v20140117-1748/fragment.properties
/usr/lib64/eclipse/plugins/org.eclipse.core.filesystem.linux.x86_64_1.2.100.v20140117-1748/os
/usr/lib64/eclipse/plugins/org.eclipse.core.filesystem.linux.x86_64_1.2.100.v20140117-1748/os/linux
/usr/lib64/eclipse/plugins/org.eclipse.core.filesystem.linux.x86_64_1.2.100.v20140117-1748/os/linux/x86_64
/usr/lib64/eclipse/plugins/org.eclipse.core.filesystem.linux.x86_64_1.2.100.v20140117-1748/os/linux/x86_64/libunixfile_1_0_0.so
/usr/lib64/eclipse/plugins/org.eclipse.core.filesystem_1.4.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.jobs_3.5.300.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.net.linux.x86_64_1.1.100.v20140117-1748
/usr/lib64/eclipse/plugins/org.eclipse.core.net.linux.x86_64_1.1.100.v20140117-1748/META-INF
/usr/lib64/eclipse/plugins/org.eclipse.core.net.linux.x86_64_1.1.100.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/plugins/org.eclipse.core.net.linux.x86_64_1.1.100.v20140117-1748/about.html
/usr/lib64/eclipse/plugins/org.eclipse.core.net.linux.x86_64_1.1.100.v20140117-1748/fragment.properties
/usr/lib64/eclipse/plugins/org.eclipse.core.net.linux.x86_64_1.1.100.v20140117-1748/libgnomeproxy-1.0.0.so
/usr/lib64/eclipse/plugins/org.eclipse.core.net.linux.x86_64_1.1.100.v20140117-1748/org
/usr/lib64/eclipse/plugins/org.eclipse.core.net.linux.x86_64_1.1.100.v20140117-1748/org/eclipse
/usr/lib64/eclipse/plugins/org.eclipse.core.net.linux.x86_64_1.1.100.v20140117-1748/org/eclipse/core
/usr/lib64/eclipse/plugins/org.eclipse.core.net.linux.x86_64_1.1.100.v20140117-1748/org/eclipse/core/net
/usr/lib64/eclipse/plugins/org.eclipse.core.net.linux.x86_64_1.1.100.v20140117-1748/org/eclipse/core/net/ProxyProvider.class
/usr/lib64/eclipse/plugins/org.eclipse.core.net_1.2.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.resources_3.8.101.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.runtime.compatibility.registry_3.5.200.v20140117-1748
/usr/lib64/eclipse/plugins/org.eclipse.core.runtime.compatibility.registry_3.5.200.v20140117-1748/.api_description
/usr/lib64/eclipse/plugins/org.eclipse.core.runtime.compatibility.registry_3.5.200.v20140117-1748/META-INF
/usr/lib64/eclipse/plugins/org.eclipse.core.runtime.compatibility.registry_3.5.200.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/plugins/org.eclipse.core.runtime.compatibility.registry_3.5.200.v20140117-1748/about.html
/usr/lib64/eclipse/plugins/org.eclipse.core.runtime.compatibility.registry_3.5.200.v20140117-1748/fragment.properties
/usr/lib64/eclipse/plugins/org.eclipse.core.runtime.compatibility.registry_3.5.200.v20140117-1748/runtime_registry_compatibility.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.runtime.compatibility_3.2.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.runtime_3.9.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.core.variables_3.2.700.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.cvs_1.4.0.v20140117-1541.jar
/usr/lib64/eclipse/plugins/org.eclipse.debug.core_3.8.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.debug.ui_3.9.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.core.commands_0.10.2.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.core.contexts_1.3.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.core.di.extensions_0.11.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.core.di_1.3.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.core.services_1.1.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.ui.bindings_0.10.101.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.ui.css.core_0.10.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.ui.css.swt.theme_0.9.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.ui.css.swt_0.11.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.ui.di_1.0.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.ui.model.workbench_1.0.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.ui.services_1.0.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.ui.widgets_1.0.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.ui.workbench.addons.swt_1.0.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.ui.workbench.renderers.swt_0.11.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.ui.workbench.swt_0.12.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.ui.workbench3_0.12.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.e4.ui.workbench_1.0.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ecf.filetransfer_5.0.0.v20130605-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ecf.identity_3.2.0.v20130605-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ecf.provider.filetransfer.httpclient4.ssl_1.0.0.v20130605-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ecf.provider.filetransfer.httpclient4_1.0.300.201303090712.jar
/usr/lib64/eclipse/plugins/org.eclipse.ecf.provider.filetransfer.ssl_1.0.0.v20130605-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ecf.provider.filetransfer_3.2.0.R-Release_HEAD-sdk_feature-77_2012-06-10_19-42-02.jar
/usr/lib64/eclipse/plugins/org.eclipse.ecf.ssl_1.1.0.v20130605-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ecf_3.2.0.v20130605-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.emf.common_2.9.1.v20130930-0823.jar
/usr/lib64/eclipse/plugins/org.eclipse.emf.ecore.change_2.9.0.v20130930-0823.jar
/usr/lib64/eclipse/plugins/org.eclipse.emf.ecore.xmi_2.9.1.v20130930-0823.jar
/usr/lib64/eclipse/plugins/org.eclipse.emf.ecore_2.9.1.v20130930-0823.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.app_1.3.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.bidi_0.10.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.common_3.6.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.concurrent_1.1.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.console_1.0.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.ds_1.4.101.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.event_1.3.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.frameworkadmin.equinox_1.0.500.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.frameworkadmin_2.0.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.http.jetty_3.0.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.http.registry_1.1.300.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.http.servlet_1.1.400.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.jsp.jasper.registry_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.jsp.jasper_1.0.400.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.launcher.gtk.linux.x86_64_1.1.200.v20140117-1748
/usr/lib64/eclipse/plugins/org.eclipse.equinox.launcher.gtk.linux.x86_64_1.1.200.v20140117-1748/META-INF
/usr/lib64/eclipse/plugins/org.eclipse.equinox.launcher.gtk.linux.x86_64_1.1.200.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/plugins/org.eclipse.equinox.launcher.gtk.linux.x86_64_1.1.200.v20140117-1748/about.html
/usr/lib64/eclipse/plugins/org.eclipse.equinox.launcher.gtk.linux.x86_64_1.1.200.v20140117-1748/eclipse_1508.so
/usr/lib64/eclipse/plugins/org.eclipse.equinox.launcher.gtk.linux.x86_64_1.1.200.v20140117-1748/launcher.gtk.linux.x86_64.properties
/usr/lib64/eclipse/plugins/org.eclipse.equinox.launcher_1.3.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.artifact.repository_1.1.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.console_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.core_2.3.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.director.app_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.director_2.3.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.directorywatcher_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.engine_2.3.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.extensionlocation_1.2.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.garbagecollector_1.0.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.jarprocessor_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.metadata.repository_1.2.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.metadata_2.2.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.operations_2.3.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.publisher.eclipse_1.1.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.publisher_1.3.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.ql_2.0.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.reconciler.dropins_1.1.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.repository.tools_2.1.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.repository_2.3.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.touchpoint.eclipse_2.1.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.touchpoint.natives_1.1.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.transport.ecf_1.1.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.ui.importexport_1.1.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.ui.sdk.scheduler_1.2.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.ui.sdk_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.ui_2.3.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.updatechecker_1.1.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.p2.updatesite_1.0.400.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.preferences_3.5.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.registry_3.5.301.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.security.ui_1.1.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.security_1.2.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.simpleconfigurator.manipulator_2.0.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.simpleconfigurator_1.0.400.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.equinox.util_1.0.500.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.help.base_4.0.0.v20140117-1541.jar
/usr/lib64/eclipse/plugins/org.eclipse.help.ui_4.0.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.help.webapp_3.6.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.help_3.6.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.jdt.core_3.9.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.jetty.continuation_9.0.5.v20130815.jar
/usr/lib64/eclipse/plugins/org.eclipse.jetty.http_9.0.5.v20130815.jar
/usr/lib64/eclipse/plugins/org.eclipse.jetty.io_9.0.5.v20130815.jar
/usr/lib64/eclipse/plugins/org.eclipse.jetty.security_9.0.5.v20130815.jar
/usr/lib64/eclipse/plugins/org.eclipse.jetty.server_9.0.5.v20130815.jar
/usr/lib64/eclipse/plugins/org.eclipse.jetty.servlet_9.0.5.v20130815.jar
/usr/lib64/eclipse/plugins/org.eclipse.jetty.util_9.0.5.v20130815.jar
/usr/lib64/eclipse/plugins/org.eclipse.jface.databinding_1.6.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.jface.text_3.8.101.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.jface_3.9.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.jsch.core_1.1.400.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.jsch.ui_1.1.400.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ltk.core.refactoring_3.6.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ltk.ui.refactoring_3.7.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.platform.doc.user_4.3.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/.api_description
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/LegacyIDE.e4xmi
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/META-INF
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/META-INF/MANIFEST.MF
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/about.html
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/about.ini
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/about.mappings
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/about.properties
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/book.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/cheatsheets
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/cheatsheets/cvs_checkout.xml
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/cheatsheets/cvs_merge.xml
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/css/e4_basestyle.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/css/e4_classic_win7.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/css/e4_classic_winxp.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/css/e4_default.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/css/e4_default_gtk.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/css/e4_default_mac.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/css/e4_default_mru_on_win7.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/css/e4_default_win7.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/css/e4_default_winxp_blu.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/css/e4_default_winxp_olv.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/disabled_book.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/eclipse16.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/eclipse16.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/eclipse256.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/eclipse32.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/eclipse32.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/eclipse48.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/eclipse48.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/eclipse_lg.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/helpData.xml
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/dragHandle.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/gtkGrey.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/gtkHandle.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/gtkTSFrame.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/macGrey.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/macHandle.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/macTSFrame.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/arrow.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/ov_teamsup48.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/ov_teamsup48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/ov_wbbasics48.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/ov_wbbasics48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/tu_checkout48.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/tu_checkout48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/tu_merge48.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/tu_merge48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/wn_eclcommunity48.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/wn_eclcommunity48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/wn_eclplatform48.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/wn_eclplatform48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/wn_migrate48.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/wn_migrate48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/wn_updates48.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/topiclabel/wn_updates48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/win7.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/win7Handle.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/win7TSFrame.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/winClassicHandle.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/winClassicTSFrame.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/winXPBluHandle.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/winXPBluTSFrame.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/winXPBlue.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/winXPHandle.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/winXPOlive.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/images/winXPTSFrame.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/intro
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/intro-eclipse.png
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/intro/css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/intro/css/overview.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/intro/css/overview.properties
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/intro/css/tutorials.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/intro/css/tutorials.properties
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/intro/css/whatsnew.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/intro/css/whatsnew.properties
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/intro/overviewExtensionContent.xml
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/intro/tutorialsExtensionContent.xml
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/intro/whatsnewExtensionContent1.xml
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/intro/whatsnewExtensionContent2.xml
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/intro/whatsnewExtensionContent3.xml
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/introData.xml
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/macosx_narrow_book.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/narrow_book.css
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/platform.jar
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/plugin.properties
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/plugin.xml
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/plugin_customization.ini
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/plugin_customization.properties
/usr/lib64/eclipse/plugins/org.eclipse.platform_4.3.1.v20140117-1541/splash.bmp
/usr/lib64/eclipse/plugins/org.eclipse.rcp_4.3.0.v20140117-1541.jar
/usr/lib64/eclipse/plugins/org.eclipse.search_3.9.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.team.core_3.7.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.team.cvs.core_3.3.500.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.team.cvs.ssh2_3.2.300.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.team.cvs.ui_3.3.600.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.team.ui_3.7.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.text_3.5.300.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.browser_3.4.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.cheatsheets_3.4.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.console_3.5.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.editors_3.8.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.externaltools_3.2.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.forms_3.6.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.ide.application_1.0.400.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.ide_3.9.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/.api_description
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/.options
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/META-INF
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/about.html
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/icons
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/icons/full
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/icons/full/elcl16
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/icons/full/elcl16/configure.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/icons/full/obj16
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/icons/full/obj16/extension_obj.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/icons/full/obj16/icallout_obj.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/icons/full/obj16/ihigh_obj.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/icons/full/obj16/ilow_obj.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/icons/full/obj16/image_obj.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/icons/full/obj16/inew_obj.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/icons/welcome16.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/introContent.xml
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/plugin.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/plugin.xml
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/contentpage
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/contentpage/fs_banner.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/contentpage/mi_banner.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/contentpage/ov_banner.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/contentpage/sa_banner.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/contentpage/tu_banner.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/contentpage/wn_banner.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/contentpage/wr_banner.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/arrow_rtl.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/content_nav_bar.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/cpt_bottomhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/cpt_midhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/firststeps.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/firststeps.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/firststeps_tophov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/fs_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/fs_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/fs_nav_64.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/fs_nav_hover.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/mi_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/mi_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/mi_nav_64.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/mi_nav_hover.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/migrate.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/migrate.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/migrate_tophov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/nav_midhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/nav_rightedgehov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/ov_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/ov_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/ov_nav_64.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/ov_nav_hover.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/ov_nav_midhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/ov_nav_rightedgehov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/overview.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/overview.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/overview_bottomhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/overview_midhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/overview_tophov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/root_bottomhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/root_midhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/root_midhov2.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/sa_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/sa_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/sa_nav_64.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/sa_nav_hover.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/sa_onesample48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/samples.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/samples.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/samples_tophov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/tu_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/tu_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/tu_nav_64.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/tu_nav_hover.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/tutorials.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/tutorials.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/tutorials_tophov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/wb_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/wb_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/wb_nav_hover.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/webresources.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/webresources.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/webresources_tophov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/whatsnew.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/whatsnew.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/whatsnew_tophov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/wn_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/wn_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/wn_nav_64.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/wn_nav_hover.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/workbench.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/workbench.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/workbench_bottomhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/workbench_midhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/workbench_tophov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/wr_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/wr_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/wr_nav_64.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/ctool/wr_nav_hover.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/obj48
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/obj48/new_obj.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/icons/obj48/newhov_obj.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/launchbar
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/launchbar/firststeps16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/launchbar/migrate16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/launchbar/overview16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/launchbar/samples16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/launchbar/tutorials16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/launchbar/webresources16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/launchbar/whatsnew16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/rootpage
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/rootpage/welcomebckgrd.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/fs_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/fs_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/mi_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/mi_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/ov_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/ov_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/sa_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/sa_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/tu_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/tu_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/wb_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/wb_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/wn_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/wn_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/wr_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/graphics/standby/wr_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/html
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/html/firststeps.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/html/font-absolute.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/html/font-relative.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/html/ltr.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/html/migrate.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/html/overview.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/html/root.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/html/rtl.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/html/samples.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/html/shared.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/html/standby.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/html/tutorials.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/html/webresources.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/html/whatsnew.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/preview.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/swt
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/swt/firststeps.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/swt/migrate.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/swt/overview.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/swt/root.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/swt/samples.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/swt/standby.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/swt/tutorials.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/swt/webresources.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/circles/swt/whatsnew.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/contentpage
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/contentpage/background.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/contentpage/backgroundcurve.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/contentpage/firsteps_wtr.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/contentpage/migrate_wtr.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/contentpage/overview_wtr.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/contentpage/samples_wtr.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/contentpage/section1.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/contentpage/section2.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/contentpage/section3.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/contentpage/section4.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/contentpage/tutorials_wtr.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/contentpage/webrsrc_wtr.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/contentpage/whatsnew_wtr.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/back.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/firsteps16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/firsteps48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/firsteps48sel.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/firsteps72.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/forward.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/home.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/migrate16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/migrate48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/migrate48sel.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/migrate72.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/overview16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/overview48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/overview48sel.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/overview72.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/samples16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/samples48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/samples48sel.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/samples72.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/tutorials16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/tutorials48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/tutorials48sel.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/tutorials72.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/wb16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/wb48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/webrsrc16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/webrsrc48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/webrsrc48sel.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/webrsrc72.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/whatsnew16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/whatsnew48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/whatsnew48sel.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/ctool/whatsnew72.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/dtool
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/dtool/back.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/dtool/forward.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/back.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/firsteps48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/firsteps48sel.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/firsteps72.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/forward.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/home.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/migrate48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/migrate48sel.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/migrate72.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/overview48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/overview48sel.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/overview72.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/samples48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/samples48sel.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/samples72.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/tutorials48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/tutorials48sel.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/tutorials72.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/wb48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/webrsrc48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/webrsrc48sel.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/webrsrc72.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/whatsnew48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/whatsnew48sel.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/etool/whatsnew72.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/obj48
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/obj48/new_obj.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/icons/obj48/newhov_obj.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/launchbar
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/launchbar/firststeps16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/launchbar/migrate16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/launchbar/overview.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/launchbar/samples.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/launchbar/tutorials.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/launchbar/webresources16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/launchbar/whatsnew.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/root
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/root/background.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/root/brandmark.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/root/dots.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/swt
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/graphics/swt/form_banner.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/html
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/html/firststeps.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/html/font-absolute.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/html/font-relative.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/html/ltr.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/html/migrate.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/html/overview.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/html/root.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/html/rtl.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/html/samples.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/html/shared.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/html/standby.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/html/tutorials.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/html/webresources.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/html/whatsnew.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/preview.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/swt
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/swt/firststeps.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/swt/migrate.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/swt/overview.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/swt/root.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/swt/samples.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/swt/standby.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/swt/tutorials.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/swt/webresources.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/purpleMesh/swt/whatsnew.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/contentpage
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/contentpage/grey_callout.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/contentpage/ov_high.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/contentpage/ov_med.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/contentpage/tu-sa_high.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/contentpage/tu-sa_med.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/contentpage/wn-fs_high.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/contentpage/wn-fs_med.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/contentpage/wr-mi_high.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/contentpage/wr-mi_med.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/icons
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/icons/ctool
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/icons/ctool/arrow.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/icons/ctool/arrow_rtl.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/icons/ctool/widget_closed.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/icons/ctool/widget_closed_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/icons/ctool/widget_closed_hov_rtl.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/icons/ctool/widget_closed_rtl.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/icons/ctool/widget_open.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/graphics/icons/ctool/widget_open_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/html
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/shared/html/shared.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/contentpage
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/contentpage/banner_extension.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/contentpage/fs_banner.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/contentpage/mi_banner.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/contentpage/ov_banner.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/contentpage/sa_banner.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/contentpage/tu_banner.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/contentpage/wn_banner.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/contentpage/wr_banner.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/arrow_rtl.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/firststeps-select.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/firststeps-select.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/firststeps.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/fs_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/fs_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/mi_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/mi_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/migrate-select.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/migrate-select.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/migrate.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/ov_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/ov_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/overview-select.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/overview-select.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/overview.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/sa_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/sa_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/samples-select.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/samples-select.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/samples.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/tu_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/tu_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/tutorials-select.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/tutorials-select.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/tutorials.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/wb_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/wb_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/webresources-select.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/webresources-select.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/webresources.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/whatsnew-select.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/whatsnew-select.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/whatsnew.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/wn_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/wn_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/workbench.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/wr_nav.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/icons/ctool/wr_nav_32.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/launchbar
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/launchbar/firststeps16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/launchbar/migrate16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/launchbar/overview16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/launchbar/samples16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/launchbar/tutorials16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/launchbar/webresources16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/launchbar/whatsnew16.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/background.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/firststeps48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/firststeps48.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/firststeps48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/firststeps48_hov.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/migrate48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/migrate48.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/migrate48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/migrate48_hov.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/overview48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/overview48.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/overview48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/overview48_hov.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/root_banner.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/root_banner_logo.jpg
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/samples48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/samples48.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/samples48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/samples48_hov.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/tutorials48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/tutorials48.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/tutorials48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/tutorials48_hov.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/webresources48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/webresources48.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/webresources48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/webresources48_hov.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/whatsnew48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/whatsnew48.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/whatsnew48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/whatsnew48_hov.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/workbench48.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/workbench48.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/workbench48_hov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/rootpage/workbench48_hov.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/fs_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/fs_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/mi_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/mi_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/ov_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/ov_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/sa_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/sa_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/tu_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/tu_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/wb_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/wb_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/wn_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/wn_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/wr_standby.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/graphics/standby/wr_standbyhov.gif
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/html
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/html/firststeps.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/html/font-absolute.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/html/font-relative.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/html/ltr.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/html/migrate.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/html/overview.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/html/root.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/html/rtl.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/html/samples.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/html/shared.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/html/standby.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/html/tutorials.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/html/webresources.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/html/whatsnew.css
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/preview.png
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/swt
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/swt/firststeps.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/swt/migrate.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/swt/overview.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/swt/root.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/swt/samples.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/swt/standby.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/swt/tutorials.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/swt/webresources.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/themes/slate/swt/whatsnew.properties
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro.universal_3.2.600.v20140117-1748/universal.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.intro_3.4.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.navigator.resources_3.4.500.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.navigator_3.5.300.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.net_1.2.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.views.properties.tabbed_3.6.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.views_3.6.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.workbench.texteditor_3.8.101.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui.workbench_3.105.1.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.ui_3.105.0.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.update.configurator_3.3.200.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.glassfish.web.javax.servlet.jsp_2.2.6.jar
/usr/lib64/eclipse/plugins/org.sat4j.core_2.3.5.v20130405.jar
/usr/lib64/eclipse/plugins/org.sat4j.pb_2.3.5.v20130405.jar
/usr/lib64/eclipse/plugins/org.w3c.css.sac_1.3.0.v200805290154.jar
/usr/lib64/eclipse/plugins/org.w3c.dom.svg_1.1.0.v200806040011.jar
/usr/lib64/eclipse/readme
/usr/lib64/eclipse/readme/readme_eclipse.html
/usr/share/appdata/eclipse.appdata.xml
/usr/share/applications/eclipse.desktop
/usr/share/eclipse
/usr/share/eclipse/dropins
/usr/share/icons/hicolor/256x256/apps/eclipse.png
/usr/share/icons/hicolor/32x32/apps/eclipse.png
/usr/share/icons/hicolor/48x48/apps/eclipse.png
/usr/share/java/eclipse/equinox.http.servlet.jar
/usr/share/maven-fragments/eclipse-platform
/usr/share/maven-poms/JPP.eclipse-equinox.http.servlet.pom
/usr/share/pixmaps
/usr/share/pixmaps/eclipse.png

#------------------------------------------------------------------------
%package	-n eclipse-equinox-osgi
Epoch:		1
Version:	4.3.1
Release:	11.0
Summary:	eclipse-equinox-osgi bootstrap version
Requires:	javapackages-bootstrap
Requires:	java >= 1:1.7.0
Requires:	jpackage-utils
Provides:	eclipse-equinox-osgi = 1:4.3.1-11.1:2014.0
Provides:	mvn(org.eclipse.osgi:org.eclipse.osgi) = 3.6.0.v20100517
Provides:	mvn(org.eclipse.osgi:org.eclipse.osgi.services) = 3.2.100.v20100503
Provides:	mvn(org.eclipse.osgi:services) = 3.2.100.v20100503
Provides:	mvn(org.eclipse.tycho:org.eclipse.osgi) = 3.6.0.v20100517
Provides:	mvn(org.eclipse:osgi) = 3.6.0.v20100517
Provides:	osgi(org.eclipse.osgi) = 3.9.1
Provides:	osgi(org.eclipse.osgi.services) = 3.3.100
Provides:	osgi(org.eclipse.osgi.util) = 3.2.300
Provides:	osgi(system.bundle) = 1:4.3.1

%description	-n eclipse-equinox-osgi
eclipse-equinox-osgi bootstrap version.

%files		-n eclipse-equinox-osgi
/usr/lib64/eclipse/plugins/org.eclipse.osgi.services_3.3.100.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.osgi.util_3.2.300.v20140117-1748.jar
/usr/lib64/eclipse/plugins/org.eclipse.osgi_3.9.1.v20140117-1748.jar
/usr/share/java/eclipse
/usr/share/java/eclipse/osgi.jar
/usr/share/java/eclipse/osgi.services.jar
/usr/share/java/eclipse/osgi.util.jar
/usr/share/maven-fragments/eclipse-equinox-osgi
/usr/share/maven-poms/JPP.eclipse-osgi.pom
/usr/share/maven-poms/JPP.eclipse-osgi.services.pom

#------------------------------------------------------------------------
%package	-n eclipse-jdt
Epoch:		1
Version:	4.3.1
Release:	11.0
Summary:	eclipse-jdt bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-cvs-client = 1:4.3.1-11.1
Requires:	eclipse-platform = 1:4.3.1-11.1
Requires:	hamcrest >= 0:1.1-11
Requires:	java-javadoc >= 1:1.7.0
Requires:	jpackage-utils
Requires:	junit >= 4.10-5
Requires:	osgi(com.ibm.icu)
Requires:	osgi(org.apache.ant)
Requires:	osgi(org.eclipse.ant.core)
Requires:	osgi(org.eclipse.compare)
Requires:	osgi(org.eclipse.core.expressions)
Requires:	osgi(org.eclipse.core.externaltools)
Requires:	osgi(org.eclipse.core.filebuffers)
Requires:	osgi(org.eclipse.core.filesystem)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.core.variables)
Requires:	osgi(org.eclipse.debug.core)
Requires:	osgi(org.eclipse.debug.ui)
Requires:	osgi(org.eclipse.equinox.bidi)
Requires:	osgi(org.eclipse.equinox.frameworkadmin)
Requires:	osgi(org.eclipse.equinox.simpleconfigurator.manipulator)
Requires:	osgi(org.eclipse.help)
Requires:	osgi(org.eclipse.jdt.core)
Requires:	osgi(org.eclipse.jface)
Requires:	osgi(org.eclipse.jface.text)
Requires:	osgi(org.eclipse.ltk.core.refactoring)
Requires:	osgi(org.eclipse.ltk.ui.refactoring)
Requires:	osgi(org.eclipse.osgi)
Requires:	osgi(org.eclipse.search)
Requires:	osgi(org.eclipse.team.core)
Requires:	osgi(org.eclipse.team.ui)
Requires:	osgi(org.eclipse.text)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.cheatsheets)
Requires:	osgi(org.eclipse.ui.console)
Requires:	osgi(org.eclipse.ui.editors)
Requires:	osgi(org.eclipse.ui.externaltools)
Requires:	osgi(org.eclipse.ui.forms)
Requires:	osgi(org.eclipse.ui.ide)
Requires:	osgi(org.eclipse.ui.intro)
Requires:	osgi(org.eclipse.ui.navigator)
Requires:	osgi(org.eclipse.ui.navigator.resources)
Requires:	osgi(org.eclipse.ui.views)
Requires:	osgi(org.eclipse.ui.workbench.texteditor)
Requires:	osgi(org.junit)
Provides:	eclipse-jdt = 1:4.3.1-11.1:2014.0
Provides:	mvn(org.eclipse.jdt:core) = 3.8.0.v_C03
Provides:	mvn(org.eclipse.jdt:org.eclipse.jdt.core) = 3.8.0.v_C03
Provides:	mvn(org.eclipse.jetty.orbit:org.eclipse.jdt.core) = 3.8.0.v_C03
Provides:	mvn(org.eclipse.tycho:org.eclipse.jdt.core) = 3.8.0.v_C03
Provides:	mvn(org.eclipse:jdt.core) = 3.8.0.v_C03
Provides:	osgi(org.eclipse.ant.launching) = 1.0.300
Provides:	osgi(org.eclipse.ant.ui) = 3.5.400
Provides:	osgi(org.eclipse.jdt) = 3.9.0
Provides:	osgi(org.eclipse.jdt.annotation) = 1.1.0
Provides:	osgi(org.eclipse.jdt.apt.core) = 3.3.500
Provides:	osgi(org.eclipse.jdt.apt.pluggable.core) = 1.0.400
Provides:	osgi(org.eclipse.jdt.apt.ui) = 3.3.300
Provides:	osgi(org.eclipse.jdt.compiler.apt) = 1.0.600
Provides:	osgi(org.eclipse.jdt.compiler.tool) = 1.0.200
Provides:	osgi(org.eclipse.jdt.core.manipulation) = 1.5.0
Provides:	osgi(org.eclipse.jdt.debug) = 3.8.0
Provides:	osgi(org.eclipse.jdt.debug.ui) = 3.6.200
Provides:	osgi(org.eclipse.jdt.doc.user) = 3.9.0
Provides:	osgi(org.eclipse.jdt.junit) = 3.7.200
Provides:	osgi(org.eclipse.jdt.junit.core) = 3.7.200
Provides:	osgi(org.eclipse.jdt.junit.runtime) = 3.4.400
Provides:	osgi(org.eclipse.jdt.junit4.runtime) = 1.1.300
Provides:	osgi(org.eclipse.jdt.launching) = 3.7.0
Provides:	osgi(org.eclipse.jdt.ui) = 3.9.1

%description	-n eclipse-jdt
eclipse-jdt bootstrap version.

%files		-n eclipse-jdt
/usr/bin/efj
/usr/lib64/eclipse/dropins/jdt
/usr/lib64/eclipse/dropins/jdt/features
/usr/lib64/eclipse/dropins/jdt/features/org.eclipse.jdt_3.9.1.v20140117-1748
/usr/lib64/eclipse/dropins/jdt/features/org.eclipse.jdt_3.9.1.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/jdt/features/org.eclipse.jdt_3.9.1.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/jdt/features/org.eclipse.jdt_3.9.1.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/dropins/jdt/features/org.eclipse.jdt_3.9.1.v20140117-1748/feature.properties
/usr/lib64/eclipse/dropins/jdt/features/org.eclipse.jdt_3.9.1.v20140117-1748/feature.xml
/usr/lib64/eclipse/dropins/jdt/features/org.eclipse.jdt_3.9.1.v20140117-1748/license.html
/usr/lib64/eclipse/dropins/jdt/plugins
/usr/lib64/eclipse/dropins/jdt/plugins/junit.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.ant.launching_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.ant.ui_3.5.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.annotation_1.1.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.apt.core_3.3.500.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.apt.pluggable.core_1.0.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.apt.ui_3.3.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.compiler.apt_1.0.600.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.compiler.tool_1.0.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.core.manipulation_1.5.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.debug.ui_3.6.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.debug_3.8.0.v20140117-1748
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.debug_3.8.0.v20140117-1748/.api_description
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.debug_3.8.0.v20140117-1748/.options
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.debug_3.8.0.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.debug_3.8.0.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.debug_3.8.0.v20140117-1748/about.html
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.debug_3.8.0.v20140117-1748/jdi.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.debug_3.8.0.v20140117-1748/jdimodel.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.debug_3.8.0.v20140117-1748/plugin.properties
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.debug_3.8.0.v20140117-1748/plugin.xml
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.doc.user_3.9.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.junit.core_3.7.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.junit.runtime_3.4.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.junit4.runtime_1.1.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.junit_3.7.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.launching_3.7.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.ui_3.9.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt_3.9.0.v20140117-1541.jar
/usr/lib64/eclipse/dropins/jdt/plugins/org.hamcrest.core_1.3.0.v201303031735.jar
/usr/share/java/eclipse/jdt.core.jar
/usr/share/maven-fragments/eclipse-jdt
/usr/share/maven-poms/JPP.eclipse-jdt.core.pom

#------------------------------------------------------------------------
%package	-n eclipse-pde
Epoch:		1
Version:	4.3.1
Release:	11.0
Summary:	eclipse-pde bootstrap version
Requires:	javapackages-bootstrap
Requires:	bash
Requires:	eclipse-jdt = 1:4.3.1-11.1
Requires:	eclipse-platform = 1:4.3.1-11.1
Requires:	objectweb-asm >= 3.3.1-1
Requires:	osgi(org.eclipse.ant.core)
Requires:	osgi(org.eclipse.ant.ui)
Requires:	osgi(org.eclipse.compare)
Requires:	osgi(org.eclipse.core.expressions)
Requires:	osgi(org.eclipse.core.filebuffers)
Requires:	osgi(org.eclipse.core.filesystem)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.core.variables)
Requires:	osgi(org.eclipse.debug.core)
Requires:	osgi(org.eclipse.debug.ui)
Requires:	osgi(org.eclipse.equinox.frameworkadmin)
Requires:	osgi(org.eclipse.equinox.frameworkadmin.equinox)
Requires:	osgi(org.eclipse.equinox.p2.artifact.repository)
Requires:	osgi(org.eclipse.equinox.p2.core)
Requires:	osgi(org.eclipse.equinox.p2.director)
Requires:	osgi(org.eclipse.equinox.p2.engine)
Requires:	osgi(org.eclipse.equinox.p2.garbagecollector)
Requires:	osgi(org.eclipse.equinox.p2.metadata)
Requires:	osgi(org.eclipse.equinox.p2.metadata.repository)
Requires:	osgi(org.eclipse.equinox.p2.operations)
Requires:	osgi(org.eclipse.equinox.p2.repository)
Requires:	osgi(org.eclipse.equinox.p2.repository.tools)
Requires:	osgi(org.eclipse.equinox.p2.touchpoint.eclipse)
Requires:	osgi(org.eclipse.equinox.p2.ui)
Requires:	osgi(org.eclipse.equinox.simpleconfigurator)
Requires:	osgi(org.eclipse.equinox.simpleconfigurator.manipulator)
Requires:	osgi(org.eclipse.help)
Requires:	osgi(org.eclipse.jdt.core)
Requires:	osgi(org.eclipse.jdt.debug)
Requires:	osgi(org.eclipse.jdt.debug.ui)
Requires:	osgi(org.eclipse.jdt.junit)
Requires:	osgi(org.eclipse.jdt.junit.core)
Requires:	osgi(org.eclipse.jdt.junit.runtime)
Requires:	osgi(org.eclipse.jdt.launching)
Requires:	osgi(org.eclipse.jdt.ui)
Requires:	osgi(org.eclipse.jface.text)
Requires:	osgi(org.eclipse.ltk.core.refactoring)
Requires:	osgi(org.eclipse.ltk.ui.refactoring)
Requires:	osgi(org.eclipse.osgi)
Requires:	osgi(org.eclipse.search)
Requires:	osgi(org.eclipse.team.core)
Requires:	osgi(org.eclipse.team.ui)
Requires:	osgi(org.eclipse.text)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.cheatsheets)
Requires:	osgi(org.eclipse.ui.console)
Requires:	osgi(org.eclipse.ui.editors)
Requires:	osgi(org.eclipse.ui.forms)
Requires:	osgi(org.eclipse.ui.ide)
Requires:	osgi(org.eclipse.ui.intro)
Requires:	osgi(org.eclipse.ui.navigator.resources)
Requires:	osgi(org.eclipse.ui.views)
Requires:	osgi(org.eclipse.ui.workbench.texteditor)
Requires:	osgi(org.eclipse.update.configurator)
Requires:	osgi(org.junit)
Requires:	osgi(org.objectweb.asm)
Requires:	zip
Provides:	eclipse = 1:4.3.1-11.1
Provides:	eclipse-pde = 1:4.3.1-11.1:2014.0
Provides:	eclipse-pde-runtime = 1:4.3.1-11.1
Provides:	eclipse-sdk = 1:4.3.1-11.1
Provides:	osgi(FRAGMENT_ID) = FRAGMENT_VERSION
Provides:	osgi(PLUGIN_ID) = PLUGIN_VERSION
Provides:	osgi(org.eclipse.ant.core.source) = 3.2.500
Provides:	osgi(org.eclipse.ant.launching.source) = 1.0.300
Provides:	osgi(org.eclipse.ant.ui.source) = 3.5.400
Provides:	osgi(org.eclipse.compare.core.source) = 3.5.300
Provides:	osgi(org.eclipse.compare.source) = 3.5.401
Provides:	osgi(org.eclipse.core.commands.source) = 3.6.100
Provides:	osgi(org.eclipse.core.contenttype.source) = 3.4.200
Provides:	osgi(org.eclipse.core.databinding.beans.source) = 1.2.200
Provides:	osgi(org.eclipse.core.databinding.observable.source) = 1.4.1
Provides:	osgi(org.eclipse.core.databinding.property.source) = 1.4.200
Provides:	osgi(org.eclipse.core.databinding.source) = 1.4.1
Provides:	osgi(org.eclipse.core.expressions.source) = 3.4.500
Provides:	osgi(org.eclipse.core.externaltools.source) = 1.0.200
Provides:	osgi(org.eclipse.core.filebuffers.source) = 3.5.300
Provides:	osgi(org.eclipse.core.filesystem.source) = 1.4.0
Provides:	osgi(org.eclipse.core.jobs.source) = 3.5.300
Provides:	osgi(org.eclipse.core.net.source) = 1.2.200
Provides:	osgi(org.eclipse.core.resources.source) = 3.8.101
Provides:	osgi(org.eclipse.core.runtime.compatibility.registry.source) = 3.5.200
Provides:	osgi(org.eclipse.core.runtime.compatibility.source) = 3.2.200
Provides:	osgi(org.eclipse.core.runtime.source) = 3.9.0
Provides:	osgi(org.eclipse.core.variables.source) = 3.2.700
Provides:	osgi(org.eclipse.debug.core.source) = 3.8.0
Provides:	osgi(org.eclipse.debug.ui.source) = 3.9.0
Provides:	osgi(org.eclipse.e4.core.commands.source) = 0.10.2
Provides:	osgi(org.eclipse.e4.core.contexts.source) = 1.3.1
Provides:	osgi(org.eclipse.e4.core.di.extensions.source) = 0.11.100
Provides:	osgi(org.eclipse.e4.core.di.source) = 1.3.0
Provides:	osgi(org.eclipse.e4.core.services.source) = 1.1.0
Provides:	osgi(org.eclipse.e4.ui.bindings.source) = 0.10.101
Provides:	osgi(org.eclipse.e4.ui.css.core.source) = 0.10.100
Provides:	osgi(org.eclipse.e4.ui.css.swt.source) = 0.11.0
Provides:	osgi(org.eclipse.e4.ui.css.swt.theme.source) = 0.9.100
Provides:	osgi(org.eclipse.e4.ui.di.source) = 1.0.0
Provides:	osgi(org.eclipse.e4.ui.model.workbench.source) = 1.0.1
Provides:	osgi(org.eclipse.e4.ui.services.source) = 1.0.1
Provides:	osgi(org.eclipse.e4.ui.widgets.source) = 1.0.0
Provides:	osgi(org.eclipse.e4.ui.workbench.addons.swt.source) = 1.0.1
Provides:	osgi(org.eclipse.e4.ui.workbench.renderers.swt.source) = 0.11.1
Provides:	osgi(org.eclipse.e4.ui.workbench.source) = 1.0.1
Provides:	osgi(org.eclipse.e4.ui.workbench.swt.source) = 0.12.1
Provides:	osgi(org.eclipse.e4.ui.workbench3.source) = 0.12.0
Provides:	osgi(org.eclipse.equinox.app.source) = 1.3.100
Provides:	osgi(org.eclipse.equinox.bidi.source) = 0.10.0
Provides:	osgi(org.eclipse.equinox.common.source) = 3.6.200
Provides:	osgi(org.eclipse.equinox.console.source) = 1.0.100
Provides:	osgi(org.eclipse.equinox.ds.source) = 1.4.101
Provides:	osgi(org.eclipse.equinox.event.source) = 1.3.0
Provides:	osgi(org.eclipse.equinox.frameworkadmin.equinox.source) = 1.0.500
Provides:	osgi(org.eclipse.equinox.frameworkadmin.source) = 2.0.100
Provides:	osgi(org.eclipse.equinox.http.jetty.source) = 3.0.100
Provides:	osgi(org.eclipse.equinox.http.registry.source) = 1.1.300
Provides:	osgi(org.eclipse.equinox.http.servlet.source) = 1.1.400
Provides:	osgi(org.eclipse.equinox.jsp.jasper.registry.source) = 1.0.300
Provides:	osgi(org.eclipse.equinox.jsp.jasper.source) = 1.0.400
Provides:	osgi(org.eclipse.equinox.p2.artifact.repository.source) = 1.1.200
Provides:	osgi(org.eclipse.equinox.p2.console.source) = 1.0.300
Provides:	osgi(org.eclipse.equinox.p2.core.source) = 2.3.0
Provides:	osgi(org.eclipse.equinox.p2.director.app.source) = 1.0.300
Provides:	osgi(org.eclipse.equinox.p2.director.source) = 2.3.0
Provides:	osgi(org.eclipse.equinox.p2.directorywatcher.source) = 1.0.300
Provides:	osgi(org.eclipse.equinox.p2.engine.source) = 2.3.0
Provides:	osgi(org.eclipse.equinox.p2.extensionlocation.source) = 1.2.100
Provides:	osgi(org.eclipse.equinox.p2.garbagecollector.source) = 1.0.200
Provides:	osgi(org.eclipse.equinox.p2.jarprocessor.source) = 1.0.300
Provides:	osgi(org.eclipse.equinox.p2.metadata.repository.source) = 1.2.100
Provides:	osgi(org.eclipse.equinox.p2.metadata.source) = 2.2.0
Provides:	osgi(org.eclipse.equinox.p2.operations.source) = 2.3.0
Provides:	osgi(org.eclipse.equinox.p2.publisher.eclipse.source) = 1.1.200
Provides:	osgi(org.eclipse.equinox.p2.publisher.source) = 1.3.0
Provides:	osgi(org.eclipse.equinox.p2.ql.source) = 2.0.100
Provides:	osgi(org.eclipse.equinox.p2.reconciler.dropins.source) = 1.1.200
Provides:	osgi(org.eclipse.equinox.p2.repository.source) = 2.3.0
Provides:	osgi(org.eclipse.equinox.p2.repository.tools.source) = 2.1.0
Provides:	osgi(org.eclipse.equinox.p2.touchpoint.eclipse.source) = 2.1.200
Provides:	osgi(org.eclipse.equinox.p2.touchpoint.natives.source) = 1.1.100
Provides:	osgi(org.eclipse.equinox.p2.transport.ecf.source) = 1.1.0
Provides:	osgi(org.eclipse.equinox.p2.ui.importexport.source) = 1.1.0
Provides:	osgi(org.eclipse.equinox.p2.ui.sdk.scheduler.source) = 1.2.0
Provides:	osgi(org.eclipse.equinox.p2.ui.sdk.source) = 1.0.300
Provides:	osgi(org.eclipse.equinox.p2.ui.source) = 2.3.0
Provides:	osgi(org.eclipse.equinox.p2.updatechecker.source) = 1.1.200
Provides:	osgi(org.eclipse.equinox.p2.updatesite.source) = 1.0.400
Provides:	osgi(org.eclipse.equinox.preferences.source) = 3.5.100
Provides:	osgi(org.eclipse.equinox.registry.source) = 3.5.301
Provides:	osgi(org.eclipse.equinox.security.source) = 1.2.0
Provides:	osgi(org.eclipse.equinox.security.ui.source) = 1.1.100
Provides:	osgi(org.eclipse.equinox.simpleconfigurator.manipulator.source) = 2.0.0
Provides:	osgi(org.eclipse.equinox.simpleconfigurator.source) = 1.0.400
Provides:	osgi(org.eclipse.equinox.util.source) = 1.0.500
Provides:	osgi(org.eclipse.help.base.source) = 4.0.0
Provides:	osgi(org.eclipse.help.source) = 3.6.0
Provides:	osgi(org.eclipse.help.ui.source) = 4.0.1
Provides:	osgi(org.eclipse.help.webapp.source) = 3.6.200
Provides:	osgi(org.eclipse.jdt.annotation.source) = 1.1.0
Provides:	osgi(org.eclipse.jdt.apt.core.source) = 3.3.500
Provides:	osgi(org.eclipse.jdt.apt.pluggable.core.source) = 1.0.400
Provides:	osgi(org.eclipse.jdt.apt.ui.source) = 3.3.300
Provides:	osgi(org.eclipse.jdt.compiler.apt.source) = 1.0.600
Provides:	osgi(org.eclipse.jdt.compiler.tool.source) = 1.0.200
Provides:	osgi(org.eclipse.jdt.core.manipulation.source) = 1.5.0
Provides:	osgi(org.eclipse.jdt.core.source) = 3.9.1
Provides:	osgi(org.eclipse.jdt.debug.source) = 3.8.0
Provides:	osgi(org.eclipse.jdt.debug.ui.source) = 3.6.200
Provides:	osgi(org.eclipse.jdt.doc.isv) = 3.9.1
Provides:	osgi(org.eclipse.jdt.junit.core.source) = 3.7.200
Provides:	osgi(org.eclipse.jdt.junit.runtime.source) = 3.4.400
Provides:	osgi(org.eclipse.jdt.junit.source) = 3.7.200
Provides:	osgi(org.eclipse.jdt.junit4.runtime.source) = 1.1.300
Provides:	osgi(org.eclipse.jdt.launching.source) = 3.7.0
Provides:	osgi(org.eclipse.jdt.ui.source) = 3.9.1
Provides:	osgi(org.eclipse.jface.databinding.source) = 1.6.200
Provides:	osgi(org.eclipse.jface.source) = 3.9.1
Provides:	osgi(org.eclipse.jface.text.source) = 3.8.101
Provides:	osgi(org.eclipse.jsch.core.source) = 1.1.400
Provides:	osgi(org.eclipse.jsch.ui.source) = 1.1.400
Provides:	osgi(org.eclipse.ltk.core.refactoring.source) = 3.6.100
Provides:	osgi(org.eclipse.ltk.ui.refactoring.source) = 3.7.100
Provides:	osgi(org.eclipse.osgi.services.source) = 3.3.100
Provides:	osgi(org.eclipse.osgi.source) = 3.9.1
Provides:	osgi(org.eclipse.osgi.util.source) = 3.2.300
Provides:	osgi(org.eclipse.pde) = 3.8.100
Provides:	osgi(org.eclipse.pde.api.tools) = 1.0.501
Provides:	osgi(org.eclipse.pde.api.tools.source) = 1.0.501
Provides:	osgi(org.eclipse.pde.api.tools.ui) = 1.0.401
Provides:	osgi(org.eclipse.pde.api.tools.ui.source) = 1.0.401
Provides:	osgi(org.eclipse.pde.build) = 3.8.100
Provides:	osgi(org.eclipse.pde.build.source) = 3.8.100
Provides:	osgi(org.eclipse.pde.core) = 3.9.1
Provides:	osgi(org.eclipse.pde.core.source) = 3.9.1
Provides:	osgi(org.eclipse.pde.doc.user) = 3.9.1
Provides:	osgi(org.eclipse.pde.ds.core) = 1.0.300
Provides:	osgi(org.eclipse.pde.ds.core.source) = 1.0.300
Provides:	osgi(org.eclipse.pde.ds.ui) = 1.0.300
Provides:	osgi(org.eclipse.pde.ds.ui.source) = 1.0.300
Provides:	osgi(org.eclipse.pde.junit.runtime) = 3.4.300
Provides:	osgi(org.eclipse.pde.junit.runtime.source) = 3.4.300
Provides:	osgi(org.eclipse.pde.launching) = 3.6.101
Provides:	osgi(org.eclipse.pde.launching.source) = 3.6.101
Provides:	osgi(org.eclipse.pde.runtime) = 3.4.400
Provides:	osgi(org.eclipse.pde.runtime.source) = 3.4.400
Provides:	osgi(org.eclipse.pde.ua.core) = 1.0.300
Provides:	osgi(org.eclipse.pde.ua.core.source) = 1.0.300
Provides:	osgi(org.eclipse.pde.ua.ui) = 1.0.300
Provides:	osgi(org.eclipse.pde.ua.ui.source) = 1.0.300
Provides:	osgi(org.eclipse.pde.ui) = 3.8.0
Provides:	osgi(org.eclipse.pde.ui.source) = 3.8.0
Provides:	osgi(org.eclipse.pde.ui.templates) = 3.4.600
Provides:	osgi(org.eclipse.pde.ui.templates.source) = 3.4.600
Provides:	osgi(org.eclipse.platform.doc.isv) = 4.3.0
Provides:	osgi(org.eclipse.platform.source) = 4.3.1
Provides:	osgi(org.eclipse.sdk) = 4.3.1
Provides:	osgi(org.eclipse.search.source) = 3.9.0
Provides:	osgi(org.eclipse.swt.gtk.linux.x86_64.source) = 3.102.1
Provides:	osgi(org.eclipse.team.core.source) = 3.7.0
Provides:	osgi(org.eclipse.team.cvs.core.source) = 3.3.500
Provides:	osgi(org.eclipse.team.cvs.ssh2.source) = 3.2.300
Provides:	osgi(org.eclipse.team.cvs.ui.source) = 3.3.600
Provides:	osgi(org.eclipse.team.ui.source) = 3.7.1
Provides:	osgi(org.eclipse.text.source) = 3.5.300
Provides:	osgi(org.eclipse.ui.browser.source) = 3.4.100
Provides:	osgi(org.eclipse.ui.cheatsheets.source) = 3.4.200
Provides:	osgi(org.eclipse.ui.console.source) = 3.5.200
Provides:	osgi(org.eclipse.ui.editors.source) = 3.8.100
Provides:	osgi(org.eclipse.ui.externaltools.source) = 3.2.200
Provides:	osgi(org.eclipse.ui.forms.source) = 3.6.1
Provides:	osgi(org.eclipse.ui.ide.application.source) = 1.0.400
Provides:	osgi(org.eclipse.ui.ide.source) = 3.9.1
Provides:	osgi(org.eclipse.ui.intro.source) = 3.4.200
Provides:	osgi(org.eclipse.ui.intro.universal.source) = 3.2.600
Provides:	osgi(org.eclipse.ui.navigator.resources.source) = 3.4.500
Provides:	osgi(org.eclipse.ui.navigator.source) = 3.5.300
Provides:	osgi(org.eclipse.ui.net.source) = 1.2.200
Provides:	osgi(org.eclipse.ui.source) = 3.105.0
Provides:	osgi(org.eclipse.ui.trace) = 1.0.100
Provides:	osgi(org.eclipse.ui.trace.source) = 1.0.100
Provides:	osgi(org.eclipse.ui.views.log) = 1.0.400
Provides:	osgi(org.eclipse.ui.views.log.source) = 1.0.400
Provides:	osgi(org.eclipse.ui.views.properties.tabbed.source) = 3.6.0
Provides:	osgi(org.eclipse.ui.views.source) = 3.6.100
Provides:	osgi(org.eclipse.ui.workbench.source) = 3.105.1
Provides:	osgi(org.eclipse.ui.workbench.texteditor.source) = 3.8.101
Provides:	osgi(org.eclipse.update.configurator.source) = 3.3.200
Obsoletes:	eclipse-pde-runtime < 1:3.3.2-20

%description	-n eclipse-pde
eclipse-pde bootstrap version.

%files		-n eclipse-pde
/usr/bin/eclipse-pdebuild
/usr/lib64/eclipse/buildscripts
/usr/lib64/eclipse/buildscripts/copy-platform
/usr/lib64/eclipse/dropins/sdk
/usr/lib64/eclipse/dropins/sdk/features
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.cvs.source_1.4.0.v20140117-1748
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.cvs.source_1.4.0.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.cvs.source_1.4.0.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.cvs.source_1.4.0.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.cvs.source_1.4.0.v20140117-1748/feature.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.cvs.source_1.4.0.v20140117-1748/feature.xml
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.cvs.source_1.4.0.v20140117-1748/license.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.e4.rcp.source_1.2.1.v20140117-1748
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.e4.rcp.source_1.2.1.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.e4.rcp.source_1.2.1.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.e4.rcp.source_1.2.1.v20140117-1748/build.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.e4.rcp.source_1.2.1.v20140117-1748/eclipse_update_120.jpg
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.e4.rcp.source_1.2.1.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.e4.rcp.source_1.2.1.v20140117-1748/feature.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.e4.rcp.source_1.2.1.v20140117-1748/feature.xml
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.e4.rcp.source_1.2.1.v20140117-1748/license.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.core.feature.source_1.2.1.v20140117-1748
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.core.feature.source_1.2.1.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.core.feature.source_1.2.1.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.core.feature.source_1.2.1.v20140117-1748/build.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.core.feature.source_1.2.1.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.core.feature.source_1.2.1.v20140117-1748/feature.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.core.feature.source_1.2.1.v20140117-1748/feature.xml
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.core.feature.source_1.2.1.v20140117-1748/license.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.extras.feature.source_1.2.0.v20140117-1748
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.extras.feature.source_1.2.0.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.extras.feature.source_1.2.0.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.extras.feature.source_1.2.0.v20140117-1748/build.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.extras.feature.source_1.2.0.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.extras.feature.source_1.2.0.v20140117-1748/feature.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.extras.feature.source_1.2.0.v20140117-1748/feature.xml
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.extras.feature.source_1.2.0.v20140117-1748/license.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.rcp.feature.source_1.2.0.v20140117-1748
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.rcp.feature.source_1.2.0.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.rcp.feature.source_1.2.0.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.rcp.feature.source_1.2.0.v20140117-1748/build.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.rcp.feature.source_1.2.0.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.rcp.feature.source_1.2.0.v20140117-1748/feature.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.rcp.feature.source_1.2.0.v20140117-1748/feature.xml
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.rcp.feature.source_1.2.0.v20140117-1748/license.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.user.ui.source_2.2.0.v20140117-1748
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.user.ui.source_2.2.0.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.user.ui.source_2.2.0.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.user.ui.source_2.2.0.v20140117-1748/build.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.user.ui.source_2.2.0.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.user.ui.source_2.2.0.v20140117-1748/feature.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.user.ui.source_2.2.0.v20140117-1748/feature.xml
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.equinox.p2.user.ui.source_2.2.0.v20140117-1748/license.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.help.source_2.0.1.v20140117-1748
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.help.source_2.0.1.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.help.source_2.0.1.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.help.source_2.0.1.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.help.source_2.0.1.v20140117-1748/feature.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.help.source_2.0.1.v20140117-1748/feature.xml
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.help.source_2.0.1.v20140117-1748/license.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.jdt.source_3.9.1.v20140117-1748
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.jdt.source_3.9.1.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.jdt.source_3.9.1.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.jdt.source_3.9.1.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.jdt.source_3.9.1.v20140117-1748/feature.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.jdt.source_3.9.1.v20140117-1748/feature.xml
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.jdt.source_3.9.1.v20140117-1748/license.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.pde.source_3.9.1.v20140117-1748
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.pde.source_3.9.1.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.pde.source_3.9.1.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.pde.source_3.9.1.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.pde.source_3.9.1.v20140117-1748/feature.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.pde.source_3.9.1.v20140117-1748/feature.xml
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.pde.source_3.9.1.v20140117-1748/license.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.pde_3.9.1.v20140117-1748
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.pde_3.9.1.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.pde_3.9.1.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.pde_3.9.1.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.pde_3.9.1.v20140117-1748/feature.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.pde_3.9.1.v20140117-1748/feature.xml
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.pde_3.9.1.v20140117-1748/license.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.platform.source_4.3.1.v20140117-1748
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.platform.source_4.3.1.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.platform.source_4.3.1.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.platform.source_4.3.1.v20140117-1748/build.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.platform.source_4.3.1.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.platform.source_4.3.1.v20140117-1748/feature.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.platform.source_4.3.1.v20140117-1748/feature.xml
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.platform.source_4.3.1.v20140117-1748/license.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.rcp.source_4.3.1.v20140117-1748
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.rcp.source_4.3.1.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.rcp.source_4.3.1.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.rcp.source_4.3.1.v20140117-1748/build.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.rcp.source_4.3.1.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.rcp.source_4.3.1.v20140117-1748/feature.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.rcp.source_4.3.1.v20140117-1748/feature.xml
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.rcp.source_4.3.1.v20140117-1748/license.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.sdk_4.3.1.v20140117-1748
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.sdk_4.3.1.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.sdk_4.3.1.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.sdk_4.3.1.v20140117-1748/epl-v10.html
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.sdk_4.3.1.v20140117-1748/feature.properties
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.sdk_4.3.1.v20140117-1748/feature.xml
/usr/lib64/eclipse/dropins/sdk/features/org.eclipse.sdk_4.3.1.v20140117-1748/license.html
/usr/lib64/eclipse/dropins/sdk/plugins
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ant.core.source_3.2.500.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ant.launching.source_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ant.ui.source_3.5.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.compare.core.source_3.5.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.compare.source_3.5.401.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.commands.source_3.6.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.contenttype.source_3.4.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.databinding.beans.source_1.2.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.databinding.observable.source_1.4.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.databinding.property.source_1.4.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.databinding.source_1.4.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.expressions.source_3.4.500.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.externaltools.source_1.0.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.filebuffers.source_3.5.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.filesystem.source_1.4.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.jobs.source_3.5.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.net.source_1.2.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.resources.source_3.8.101.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.runtime.compatibility.registry.source_3.5.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.runtime.compatibility.source_3.2.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.runtime.source_3.9.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.core.variables.source_3.2.700.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.debug.core.source_3.8.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.debug.ui.source_3.9.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.core.commands.source_0.10.2.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.core.contexts.source_1.3.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.core.di.extensions.source_0.11.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.core.di.source_1.3.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.core.services.source_1.1.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.ui.bindings.source_0.10.101.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.ui.css.core.source_0.10.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.ui.css.swt.source_0.11.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.ui.css.swt.theme.source_0.9.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.ui.di.source_1.0.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.ui.model.workbench.source_1.0.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.ui.services.source_1.0.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.ui.widgets.source_1.0.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.ui.workbench.addons.swt.source_1.0.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.ui.workbench.renderers.swt.source_0.11.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.ui.workbench.source_1.0.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.ui.workbench.swt.source_0.12.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.e4.ui.workbench3.source_0.12.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.app.source_1.3.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.bidi.source_0.10.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.common.source_3.6.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.console.source_1.0.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.ds.source_1.4.101.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.event.source_1.3.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.frameworkadmin.equinox.source_1.0.500.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.frameworkadmin.source_2.0.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.http.jetty.source_3.0.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.http.registry.source_1.1.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.http.servlet.source_1.1.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.jsp.jasper.registry.source_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.jsp.jasper.source_1.0.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.artifact.repository.source_1.1.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.console.source_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.core.source_2.3.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.director.app.source_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.director.source_2.3.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.directorywatcher.source_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.engine.source_2.3.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.extensionlocation.source_1.2.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.garbagecollector.source_1.0.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.jarprocessor.source_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.metadata.repository.source_1.2.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.metadata.source_2.2.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.operations.source_2.3.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.publisher.eclipse.source_1.1.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.publisher.source_1.3.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.ql.source_2.0.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.reconciler.dropins.source_1.1.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.repository.source_2.3.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.repository.tools.source_2.1.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.touchpoint.eclipse.source_2.1.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.touchpoint.natives.source_1.1.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.transport.ecf.source_1.1.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.ui.importexport.source_1.1.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.ui.sdk.scheduler.source_1.2.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.ui.sdk.source_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.ui.source_2.3.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.updatechecker.source_1.1.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.p2.updatesite.source_1.0.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.preferences.source_3.5.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.registry.source_3.5.301.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.security.source_1.2.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.security.ui.source_1.1.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.simpleconfigurator.manipulator.source_2.0.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.simpleconfigurator.source_1.0.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.equinox.util.source_1.0.500.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.help.base.source_4.0.0.v20140117-1541.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.help.source_3.6.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.help.ui.source_4.0.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.help.webapp.source_3.6.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.annotation.source_1.1.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.apt.core.source_3.3.500.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.apt.pluggable.core.source_1.0.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.apt.ui.source_3.3.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.compiler.apt.source_1.0.600.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.compiler.tool.source_1.0.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.core.manipulation.source_1.5.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.core.source_3.9.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.debug.source_3.8.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.debug.ui.source_3.6.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.doc.isv_3.9.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.junit.core.source_3.7.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.junit.runtime.source_3.4.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.junit.source_3.7.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.junit4.runtime.source_1.1.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.launching.source_3.7.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jdt.ui.source_3.9.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jface.databinding.source_1.6.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jface.source_3.9.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jface.text.source_3.8.101.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jsch.core.source_1.1.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.jsch.ui.source_1.1.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ltk.core.refactoring.source_3.6.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ltk.ui.refactoring.source_3.7.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.osgi.services.source_3.3.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.osgi.source_3.9.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.osgi.util.source_3.2.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.api.tools.source_1.0.501.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.api.tools.ui.source_1.0.401.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.api.tools.ui_1.0.401.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.api.tools_1.0.501.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build.source_3.8.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/.api_description
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/.options
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/META-INF
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/META-INF/eclipse.inf
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/about.html
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/about_files
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/about_files/LICENSE-2.0.txt
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data/21
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data/21/fragment
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data/21/fragment/fragment.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data/21/plugin
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data/21/plugin/plugin.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data/30
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data/30/fragment
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data/30/fragment/META-INF
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data/30/fragment/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data/30/fragment/fragment.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data/30/plugin
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data/30/plugin/META-INF
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data/30/plugin/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data/30/plugin/plugin.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/data/env.properties
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/lib
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/lib/pdebuild-ant.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/pdebuild.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/plugin.properties
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/plugin.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/scripts
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/scripts/build.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/scripts/genericTargets.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/scripts/package.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/scripts/productBuild
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/scripts/productBuild/allElements.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/scripts/productBuild/productBuild.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/features
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/features/customBuildCallbacks.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/headless-build
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/headless-build/allElements.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/headless-build/build.properties
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/headless-build/customAssembly.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/headless-build/customTargets.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/package-build
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/package-build/build.properties
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/package-build/customTargets-assemble-target.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/package-build/customTargets.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/package-build/prepare-build-dir.sh
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/packager
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/packager/customTargets.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/packager/packager.properties
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/packager/packaging.properties
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/plugins
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.build_3.8.100.v20140117-1748/templates/plugins/customBuildCallbacks.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.core.source_3.9.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.core_3.9.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.doc.user_3.9.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.ds.core.source_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.ds.core_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.ds.ui.source_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.ds.ui_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.junit.runtime.source_3.4.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.junit.runtime_3.4.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.launching.source_3.6.101.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.launching_3.6.101.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.runtime.source_3.4.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.runtime_3.4.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.ua.core.source_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.ua.core_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.ua.ui.source_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.ua.ui_1.0.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.ui.source_3.8.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.ui.templates.source_3.4.600.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.ui.templates_3.4.600.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde.ui_3.8.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.pde_3.8.100.v20140117-1541.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.platform.doc.isv_4.3.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.platform.source_4.3.1.v20140117-1541.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/META-INF
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/META-INF/MANIFEST.MF
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/about.html
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/about.ini
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/about.mappings
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/about.properties
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/book.css
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/disabled_book.css
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/eclipse16.gif
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/eclipse16.png
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/eclipse256.png
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/eclipse32.gif
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/eclipse32.png
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/eclipse48.gif
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/eclipse48.png
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/eclipse_lg.gif
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/helpData.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/intro-eclipse.png
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/introData.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/macosx_narrow_book.css
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/narrow_book.css
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/plugin.properties
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/plugin.xml
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/plugin_customization.ini
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.sdk_4.3.1.v20140117-1541/plugin_customization.properties
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.search.source_3.9.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.swt.gtk.linux.x86_64.source_3.102.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.team.core.source_3.7.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.team.cvs.core.source_3.3.500.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.team.cvs.ssh2.source_3.2.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.team.cvs.ui.source_3.3.600.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.team.ui.source_3.7.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.text.source_3.5.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.browser.source_3.4.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.cheatsheets.source_3.4.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.console.source_3.5.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.editors.source_3.8.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.externaltools.source_3.2.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.forms.source_3.6.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.ide.application.source_1.0.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.ide.source_3.9.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.intro.source_3.4.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.intro.universal.source_3.2.600.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.navigator.resources.source_3.4.500.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.navigator.source_3.5.300.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.net.source_1.2.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.source_3.105.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.trace.source_1.0.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.trace_1.0.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.views.log.source_1.0.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.views.log_1.0.400.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.views.properties.tabbed.source_3.6.0.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.views.source_3.6.100.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.workbench.source_3.105.1.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.ui.workbench.texteditor.source_3.8.101.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.eclipse.update.configurator.source_3.3.200.v20140117-1748.jar
/usr/lib64/eclipse/dropins/sdk/plugins/org.objectweb.asm_3.3.1.jar

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
rpm2cpio %{SOURCE1} | cpio -id
rpm2cpio %{SOURCE2} | cpio -id
rpm2cpio %{SOURCE3} | cpio -id
mkdir -p %{buildroot}/usr/lib/java
cp -p %{SOURCE4} %{buildroot}/usr/lib64/eclipse
ln -sf /usr/lib64/eclipse %{buildroot}/usr/lib/eclipse
ln -sf /usr/lib64/eclipse/swt.jar %{buildroot}/usr/lib/java
