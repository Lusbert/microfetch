# color codes and logos stolen form https://github.com/cappsyco/tzyfetch/
import os
import socket

os_dict = {
    "adelie"               :  "\\033[1;31m_/\\`",
    "almalinux"            :  "\\033[1;34m{X}",
    "alpine"               :  "\\033[1;34m<^>",
    "altlinux"             :  "\\033[1;33mr,l",
    "amzn"                 :  "\\033[1;33m|Y|",
    "anarchy"              :  "\\033[1;34m/-\\\\",
    "anduinos"             :  "\\033[1;34m<•>",
    "arch"                 :  "\\033[1;34m/.\\\\",
    "arch32"               :  "\\033[1;34m/.\\\\",
    "archbang"             :  "\\033[1;32m/!\\\\",
    "archcraft"            :  "\\033[1;34m/x\\\\",
    "archman"              :  "\\033[1;31m/*\\\\",
    "arcolinux"            :  "\\033[1;34m/,\\\\",
    "arkane"               :  "\\033[1;31m^,^",
    "artix"                :  "\\033[1;34m/>\\\\",
    "bazzite"              :  "\\033[1;35mΓ+)",
    "blackarch"            :  "\\033[1;94m/|\\\\",
    "blendos"              :  "\\033[1;32m(B)",
    "bodhi"                :  "\\033[1;32m'\\\\",
    "cachyos"              :  "\\033[1;32mC:\\`",
    "centos"               :  "\\033[1;34m<+>",
    "centos_stream"        :  "\\033[1;34m<+>",
    "chimera"              :  "\\033[1;31m[cL",
    "chimeraos"            :  "\\033[1;31m°w°",
    "chromeos"             :  "\\033[1;34m(o)",
    "clear"                :  "\\033[1;94m|Γ",
    "debian"               :  "\\033[1;31m(@)",
    "Deepin"               :  "\\033[1;94m(%)",
    "devuan"               :  "\\033[1;31m>cv",
    "dragonfly"            :  "\\033[1;31m=I=",
    "elementary"           :  "\\033[1;94m(e)",
    "endeavouros"          :  "\\033[1;35m|D)",
    "endless"              :  "\\033[1;33md\\\\p",
    "eurolinux"            :  "\\033[1;34m(-)",
    "exherbo"              :  "\\033[1;37m°o°",
    "fedora"               :  "\\033[1;34m(f)",
    "fedoraremixforwsl"    :  "\\033[1;34m(f)",
    "freebsd"              :  "\\033[1;31m^O^",
    "funtoo"               :  "\\033[1;35mf°°",
    "garuda"               :  "\\033[1;34mo\\`>",
    "gentoo"               :  "\\033[1;90m>°>",
    "ghostbsd"             :  "\\033[1;34m(G)",
    "gnoppix"              :  "\\033[1;34m(G)",
    "guix"                 :  "\\033[1;33m\\`V\\`",
    "hyperbola"            :  "\\033[1;37m/H/",
    "kali"                 :  "\\033[1;94m3c\\`",
    "kaos"                 :  "\\033[1;34ml<.",
    "linuxmint"            :  "\\033[1;32mlm)",
    "mageia"               :  "\\033[1;34m(°)",
    "manjaro"              :  "\\033[1;32m(M)",
    "manjaro-arm"          :  "\\033[1;32m(M)",
    "miraclelinux"         :  "\\033[1;32ml|l",
    "neon"                 :  "\\033[1;94m(•)",
    "nilrt"                :  "\\033[1;32m[n]",
    "nixos"                :  "\\033[1;34m<=>",
    "nobara"               :  "\\033[1;37mn•>",
    "ol"                   :  "\\033[1;31m(_)",
    "omnios"               :  "\\033[1;37m\\\\\\`>",
    "openmandriva"         :  "\\033[1;34m((o",
    "opensuse"             :  "\\033[1;32m@n>",
    "opensuse-leap"        :  "\\033[1;32m\\\\^/",
    "opensuse-tumbleweed"  :  "\\033[1;94mo/o",
    "suse"                 :  "\\033[1;32m@n>",
    "openwrt"              :  "\\033[1;94m(V)",
    "parrot"               :  "\\033[1;32m<\\\\^",
    "pclinuxos"            :  "\\033[1;34m(v)",
    "pengwin"              :  "\\033[1;35m(p)",
    "photon"               :  "\\033[1;90m(:)",
    "pika"                 :  "\\033[1;33m•,•",
    "pisilinux"            :  "\\033[1;35m^v^",
    "pop"                  :  "\\033[1;94mP!_",
    "puppy"                :  "\\033[1;34m:>}",
    "pureos"               :  "\\033[1;34mPOS",
    "raspbian"             :  "\\033[1;31m'O'",
    "rebornos"             :  "\\033[1;94m<X>",
    "redox"                :  "\\033[1;94m(R)",
    "rhel"                 :  "\\033[1;31m_n_",
    "rocky"                :  "\\033[1;32m(/,",
    "slackware"            :  "\\033[1;94m(S)",
    "sled"                 :  "\\033[1;32m@n>",
    "sles"                 :  "\\033[1;32m@n>",
    "solaris"              :  "\\033[1;31m\\\\|/",
    "solus"                :  "\\033[1;34m|\\\\)",
    "steamos"              :  "\\033[1;35m•))",
    "tails"                :  "\\033[1;35m:Dc",
    "tencent"              :  "\\033[1;31m\\\\//",
    "tinycore"             :  "\\033[1;90m(/)",
    "trisquel"             :  "\\033[1;34m@Y@",
    "ubuntu"               :  "\\033[1;33m{•}",
    "ultramarine"          :  "\\033[1;34m(;)",
    "vanillaos"            :  "\\033[1;33m>*<",
    "virtuozzo"            :  "\\033[1;31m\\\\z/",
    "void"                 :  "\\033[1;32m(\\\\)",
    "wolfi"                :  "\\033[1;31m,O,",
    "zorin"                :  "\\033[1;34m<Z>",
}
def get_os_id():
    try:
        with open("/etc/os-release", "r") as f:
            for line in f:
                key, _, value = line.partition("=")
                if key.strip() == "ID":
                    return value.strip().strip('"')
    except FileNotFoundError:
        return "Unknown ID"

def get_os_name():
    try:
        with open("/etc/os-release", "r") as f:
            for line in f:
                key, _, value = line.partition("=")
                if key.strip() == "NAME":
                    return value.strip().strip('"')
    except FileNotFoundError:
        return "Unknown NAME"



def generate_output():
    os_id   = get_os_id()
    os_logo = os_dict.get(os_id, f"Unknown OS ({os_id})")
    name    = get_os_name()

    # User and hostname
    user = os.getlogin()
    hostname = socket.gethostname()
    user_hostname = f"{user}@{hostname}"

    # Generate the final string
    gen_string = f"{os_logo} {name} \\033[1;90m:: {user_hostname}\\n"
    output =f"""#include <stdio.h>

int main(void) {{
    printf("{gen_string}");
    return 0;
}}
"""
    return output

if __name__ == "__main__":
    print(generate_output())
    output = generate_output()
    with open("source.c", "w") as file:
                file.write(output)
