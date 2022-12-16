class dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.size = 0
        self.total_size = 0
        self.parent = parent
        self.files = {}
        self.subdir = {}
        self.count = 0
        self.large = False

    def get_name(self):
        return self.name

    def add_parent_size(self, size):
        if self.parent != None:
            self.parent.total_size += size
            self.parent.check_size()
            self.parent.add_parent_size(size)

    def add_file(self, name, size):
        if name not in self.files:
            self.files[name] = size
            self.size += size
            self.total_size += size
            self.check_size()
            self.add_parent_size(size)


    def check_size(self):
        if self.total_size >= 100000 and self.large == False:
            self.count += 1
            self.large = True
    
    def add_subdir(self, name):
        if name not in self.subdir:
            self.subdir[dir(name, self)] = 0
            

    def get_size(self):
        return self.size
    
    def get_total_size(self):
        return self.total_size

    def get_subdir(self):
        return self.subdir

    def cd(self, name):
        if name == '/':
            return self
        if name == '.':
            return self
        elif name == '..':
            if self.parent == None:
                return self
            return self.parent
        else:
            for i in self.subdir:
                if i.name == name:
                    return i

    
    def ls(self):
        return self.subdir + list(self.files.keys())
            


with open("Day7/input.txt") as f: 
    lines = f.readlines()


def main():
    s = {}
    current_dir = dir('/')
    cc = ''
    for line in lines:
        line = line.strip()
        if line[0] == '$': # command
            if cc == 'ls':
                #print("{} {}".format(current_dir.get_size(), current_dir.get_name()))
                if current_dir.get_total_size() >= 100000 and current_dir.get_name() not in s:
                    s[current_dir.get_name()] = current_dir.get_total_size()
                elif current_dir.get_total_size() >= 100000 and current_dir.get_name() in s:
                    s[current_dir.get_name()] = current_dir.get_total_size()
            cc = line[2:4].strip()
            #print(cc)
            if cc == 'cd':
                if line.split(" ")[2] == '/':
                    continue
                else:
                    current_dir = current_dir.cd(line.split(" ")[2])
            elif cc == 'ls':
                continue
        elif line[0] != '$' and cc == 'ls':
            if line[0] == 'd':
                current_dir.add_subdir(line.split(" ")[1])
            else:
                current_dir.add_file(line.split(' ')[1].strip(), int(line.split(' ')[0]))


    while current_dir.parent != None:
        current_dir = current_dir.cd('..')

    print(current_dir.get_total_size())


if __name__ == "__main__":
    main()

