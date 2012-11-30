#!/bin/bash

for file in `ls *tagged.txt | sort -g` 
do
	trained=`echo $file | sed s/tagged/train/`
	parsed=`echo $file | sed s/tagged/parsed/`
	annotated=`echo $file | sed s/tagged/annotated/`
	pwd=`pwd`
	pushd /home/amber/Downloads/Downloads/IllinoisNerExtended-v2.1
	trainInfo=`echo $file | sed s/tagged/trainInfo/`
	testResults=`echo $file | sed s/tagged/output/`
	time java -classpath lib/LBJ-2.8.2.jar:lib/LBJLibrary-2.8.2.jar:dist/LbjNerTagger-2.1.jar -Xmx2000m edu.illinois.cs.cogcomp.LbjNer.LbjTagger.NerTagger -train $pwd/$trained -test $pwd/$file -c true DemoConfig/ner.conll.config &> $pwd/$trainInfo
	java -classpath lib/LBJ-2.8.2.jar:lib/LBJLibrary-2.8.2.jar:dist/LbjNerTagger-2.1.jar -Xmx2000m edu.illinois.cs.cogcomp.LbjNer.LbjTagger.NerTagger -test $pwd/$file -c true DemoConfig/ner.conll.config &> $pwd/$testResults
	popd
	pushd /home/amber/Downloads/Downloads/IllinoisNerExtended-v2.1-orig
	lbjResults=`echo $file | sed s/tagged/lbj/`
	java -classpath lib/LBJ-2.8.2.jar:lib/LBJLibrary-2.8.2.jar:dist/LbjNerTagger-2.1.jar -Xmx2000m edu.illinois.cs.cogcomp.LbjNer.LbjTagger.NerTagger -test $pwd/$file -c true DemoConfig/ner.conll.config &> $pwd/$lbjResults
	popd
done
