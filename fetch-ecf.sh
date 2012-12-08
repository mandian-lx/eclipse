#!/bin/sh

for f in \
    org.eclipse.ecf \
    org.eclipse.ecf.core.identity \
    org.eclipse.ecf.filetransfer \
    org.eclipse.ecf.provider.filetransfer \
    org.eclipse.ecf.provider.filetransfer.ssl \
    org.eclipse.ecf.ssl \
; do
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/technology \
export -r v20080611-1715 org.eclipse.ecf/plugins/$f;
done

tar cjf ecf-filetransfer-v20080611-1715.tar.bz2 org.eclipse.ecf
