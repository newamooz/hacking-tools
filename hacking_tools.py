import subprocess , os
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[1;31m'+r"""


              _______  _______  _       _________ _        _______    _________ _______  _______  _        _______ 
    |\     /|(  ___  )(  ____ \| \    /\\__   __/( (    /|(  ____ \   \__   __/(  ___  )(  ___  )( \      (  ____ \
    | )   ( || (   ) || (    \/|  \  / /   ) (   |  \  ( || (    \/      ) (   | (   ) || (   ) || (      | (    \/
    | (___) || (___) || |      |  (_/ /    | |   |   \ | || |      _____ | |   | |   | || |   | || |      | (_____ 
    |  ___  ||  ___  || |      |   _ (     | |   | (\ \) || | ____(_____)| |   | |   | || |   | || |      (_____  )
    | (   ) || (   ) || |      |  ( \ \    | |   | | \   || | \_  )      | |   | |   | || |   | || |            ) |
    | )   ( || )   ( || (____/\|  /  \ \___) (___| )  \  || (___) |      | |   | (___) || (___) || (____/\/\____) |
    |/     \||/     \|(_______/|_/    \/\_______/|/    )_)(_______)      )_(   (_______)(_______)(_______/\_______)
                                                                                                                   

    Tblak : ) 
    """)
    print('\033[1;37m'+ """

    +=========================================+
    |    [*] - nmap       [*] - wireshark     |
    |    [*] - hydra      [*] - netcat        |
    |    [*] - fping      [*] - crunch        |
    |    [*] - sqlmap     [*] - airecrack-ng  |
    |    [*] - wifite     [*] - ophcrack      |
    |    [*] - john       [*] - masscan       |
    |    [*] - yersinia   [*] - tcpdump       |
    |    [*] - ettercap   [*] - nikto         |
    |    [*] - whatweb    [*] - wfuzz         |
    |    [*] - macchanger [*] - bettercap     |
    |    [*] - tkhunter   [*] - dnsiff        |
    |    [*] - netdiscover[*] - hping3        |
    |    [*] - apktool    [*] - pdfcrack      |
    |    [*] - hashcat    [*] - fcrackzip     |
    |    [*] - cewl       [*] - p0f           |
    |    [*] - openVAS    [*] - Bully         |
    |    [*] - openssl    [*] - openvpn       |
    +=========================================+
    """)
    number = input('\033[1;33m'+"Do you want to continue? y/n >>")
    if number == "n":
        break
    elif number == "y":
        def run_command(command):
            try:
                result = subprocess.run(command, shell=True, check=True, text=True)
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
                print(e.stderr)
        wireshark_install_command = "sudo apt install wireshark"
        run_command(wireshark_install_command)
        nmap_install_command = "sudo apt install nmap"
        run_command(nmap_install_command)
        hydra_install_command = "sudo apt install hydra-gtk"
        run_command(hydra_install_command)
        nc_install_command = "sudo apt install netcat"
        run_command(nc_install_command)
        fping_install_command = "sudo apt install fping"
        run_command(fping_install_command)
        cu_install_command = "sudo apt install crunch"
        run_command(cu_install_command)
        sql_install_command = "sudo apt install sqlmap"
        run_command(sql_install_command)
        aire_install_command = "sudo apt install aircrack-ng"
        run_command(aire_install_command)
        wifite_install_command = "sudo apt install wifite"
        run_command(wifite_install_command)
        ophcrack_install_command = "sudo apt install ophcrack"
        run_command(ophcrack_install_command)
        john_install_command = "sudo apt install john"
        run_command(john_install_command)
        mass_install_command = "sudo apt install masscan"
        run_command(mass_install_command)
        yer_install_command = "sudo apt install yersinia"
        run_command(yer_install_command)
        tcp_install_command = "sudo apt install tcpdump"
        run_command(tcp_install_command)
        ettr_install_command = "sudo apt install ettercap-graphical"
        run_command(ettr_install_command)
        nikto_install_command = "sudo apt install nikto"
        run_command(nikto_install_command)
        whatw_install_command = "sudo apt install whatweb"
        run_command(whatw_install_command)
        wfuzz_install_command = "sudo apt install wfuzz"
        run_command(wfuzz_install_command)
        mac_install_command = "sudo apt install macchanger"
        run_command(mac_install_command)
        better_install_command = "sudo apt install bettercap"
        run_command(better_install_command)
        rkhunter_install_command = "sudo apt install rkhunter"
        run_command(rkhunter_install_command)
        dsniff_install_command = "sudo apt install dsniff"
        run_command(dsniff_install_command)
        net_install_command = "sudo apt install netdiscover"
        run_command(net_install_command)
        hping_install_command = "sudo apt install hping3"
        run_command(hping_install_command)
        apk_install_command = "sudo apt install apktool"
        run_command(apk_install_command)
        dns_install_command = "sudo apt install dnsmap"
        run_command(dns_install_command)
        pdf_install_command = "sudo apt install pdfcrack"
        run_command(pdf_install_command)
        cat_install_command = "sudo apt install hashcat"
        run_command(cat_install_command)
        zip_install_command = "sudo apt install fcrackzip"
        run_command(zip_install_command)
        cewl_install_command = "sudo apt install cewl"
        run_command(cewl_install_command)
        p0f_install_command = "sudo apt install p0f"
        run_command(p0f_install_command)
        vas_install_command = "sudo apt install openvas"
        run_command(vas_install_command)
        bully_install_command = "sudo apt install bully"
        run_command(bully_install_command)
        openssl_install_command = "sudo apt install openssl"
        run_command(openssl_install_command)
        openvpn_install_command = "sudo apt install openvpn"
        run_command(openvpn_install_command)
        print("The installation is complete")
    else:
        print("Invalid input Please enter 'y' or 'n' >>")


