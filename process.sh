#!/bin/bash

for file in `ls *tagged.txt | sort -g` 
do
	trained=`echo $file | sed s/tagged/train/`
	parsed=`echo $file | sed s/tagged/parsed/`
	annotated=`echo $file | sed s/tagged/annotated/`
	pwd=`pwd`
	pushd /home/ab6/Downloads/IllinoisNerExtended-v2.1
	java -classpath lib/LBJ-2.8.2.jar:lib/LBJLibrary-2.8.2.jar:dist/LbjNerTagger-2.1.jar -Xmx2000m edu.illinois.cs.cogcomp.LbjNer.LbjTagger.NerTagger -train $pwd/$trained -test $pwd/$file -c true DemoConfig/ner.conll.config
	java -classpath lib/LBJ-2.8.2.jar:lib/LBJLibrary-2.8.2.jar:dist/LbjNerTagger-2.1.jar -Xmx2000m edu.illinois.cs.cogcomp.LbjNer.LbjTagger.NerTagger -annotate $pwd/$parsed $pwd/$annotated true DemoConfig/ner.conll.config
	echo >> $pwd/output.txt
	cat $pwd/$annotated >> $pwd/output.txt
	popd
done