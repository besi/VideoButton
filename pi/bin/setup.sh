sudo cp etc/video-button.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable video-button
sudo systemctl start video-button

