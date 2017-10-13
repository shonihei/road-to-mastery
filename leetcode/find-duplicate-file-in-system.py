"""
Given a list of directory info including directory path, and all the files with contents in this directory,
you need to find out all the groups of duplicate files in the file system in terms of their paths.

A group of duplicate files consists of at least two files that have exactly the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content, f2_content ... fn_content,
respectively) in directory root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of group of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"
"""

def findDuplicates(paths):
    contents = {}
    for _dir in paths:
        _dir = _dir.split()
        path = _dir[0]
        for file in _dir[1:]:
            filename, content = file.split("(")
            contents.setdefault(content[:-1], []).append(path + "/" + filename)
    out = []
    for content, dupes in contents.items():
        if len(dupes) > 1:
            out.append(dupes)
    return out

if __name__ == "__main__":
    import unittest
    
    class Test(unittest.TestCase):
        def test1(self):
            _in = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
            out = [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
            self.assertCountEqual(findDuplicates(_in), out)

    unittest.main()
