rm pipe
mkfifo pipe
echo '1000000' > data/fa_balance
tail -f pipe | python3 fundingAgency.py


