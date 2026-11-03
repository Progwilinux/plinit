require "./funcs/logs"
require "./funcs/storage"

arg = ARGV.at(0)?
disk = ARGV.at(1)?

case arg
when "--disk"
    Storage.mount_all
    system("/etc/plinit/other.sh")

    loop do
        system("/bin/sh -i")
        Logs.log("Omagad!")
        sleep 2
    end
when "--initrd"
    Storage.mount("sysfs", "/sys")
    Storage.mount("proc", "/proc")
    Storage.mount("devtmpfs", "/dev")

    case disk
    when "none", nil
        Logs.warn("No disk...")

        loop do
            system("/bin/sh -i")
            Logs.log("Omagad!")
            sleep 2
        end
    else
        if File.exists?(disk)
            Dir.mkdir_p("amogus")

            system("mount #{disk} /amogus")

            Storage.mount_move("/sys", "/amogus/sys")
            Storage.mount_move("/proc", "/amogus/proc")
            Storage.mount_move("/dev", "/amogus/dev")

            system("chroot /amogus/sbin/plinit --disk")
        else
            Logs.err("Disk not found.")
        end
    end
when nil
    Logs.err("...")
else
    Logs.err("Unknown argument.")
end