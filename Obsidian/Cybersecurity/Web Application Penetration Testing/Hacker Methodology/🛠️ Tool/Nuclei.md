
Linkes:
- https://github.com/projectdiscovery/nuclei
- https://github.com/projectdiscovery/nuclei-templates
- https://github.com/SirBugs/Priv8-Nuclei-Templates
- https://github.com/boobooHQ/private_templates


----------
export PATH=$PATH:$HOME/go/bin source ~/.bashrc
----------------------------------------------------------------------------------------------


sudo apt install -y nuclei &>/dev/null
nuclei -validate
nuclei -u http://example.com -t ~/nuclei-templates
