require "./logs"

module Storage
  def self.mount(type : String, path : String)
    Logs.log("Moounting #{path}...")
    system("mount -t #{type} #{type} #{path}")
  rescue ex
    Logs.err("Something went wrong... #{ex.message}")
  end

  def self.mount_all
    Logs.log("Moounting fstab...")
    system("mount -a")
  rescue ex
    Logs.err("Something went wrong... #{ex.message}")
  end

  def self.mount_move(path : String, target : String)
    Logs.log("Moount --move #{path}...")
    system("mount --move #{path} #{target}#{path}")
  rescue ex
    Logs.err("Something went wrong... #{ex.message}")
  end
end
