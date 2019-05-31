echo "================= CMSRUN starting ===================="
cmsRun -j FrameworkJobReport.xml -p PSet.py 
cmsRun -n 4 step2.py
cmsRun -n 4 step3.py
echo "================= CMSRUN finished ===================="
