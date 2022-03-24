cp pi/etc/dot.bashrc ~/.bashrc

sudo cp etc/video-button.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable video-button
sudo systemctl start video-button

sudo cp etc/software-update.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable software-update
sudo systemctl start software-update
