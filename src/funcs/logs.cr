module Logs
    def self.log(msg : String)
        puts "[PLINIT:log]: #{msg}"
    end

    def self.warn(msg : String)
        puts "[PLINIT:warn]: #{msg}"
    end

    def self.err(msg : String)
        puts "[PLINIT:err]: #{msg}"
    end
end