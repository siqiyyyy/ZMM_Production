echo "================= CMSRUN starting ===================="
cmsRun -j FrameworkJobReport.xml -p PSet.py &> log_step0.txt
cmsRun -n 4 step2.py &> log_step2.txt
cmsRun -n 4 step3.py &> log_step3.txt
echo "================= CMSRUN finished ===================="
