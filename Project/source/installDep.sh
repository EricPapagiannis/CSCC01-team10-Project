current=$(pip list | grep "requests (2")

if [ -z "$current" ]; then

    echo installing requests
    pip3 install requests
    echo "installed requests"

else

    echo "Requests already installed"

fi

`brew>temp`
if test `read temp` == "The program \'brew\' is currently not installed. You can install it by typing:\nsudo apt install linuxbrew-wrapper\n"
then
	echo installing brew
	sudo apt install linuxbrew-wrapper
	echo installed brew
else
	echo brew already installed
fi

`brew list | grep hub>temp`
if test `read temp` == 'hub'
then
	echo hub already installed
else
	echo installing hub
	git clone https://github.com/github/hub.git && cd hub
	script/build
	echo installed hub
fi

echo
echo installation complete
