use crate::Solution;
use std::{
    collections::HashMap,
    fs::{self},
};

pub struct Day {
    pub input_path: String,
}

type FileId = usize;

struct FileSystem {
    nodes: HashMap<FileId, FileNode>,
    fid_counter: usize,
}

impl FileSystem {
    fn new() -> FileSystem {
        let mut h = HashMap::new();
        h.insert(
            0,
            FileNode {
                fid: 0,
                name: "/".to_string(),
                size: 0,
                children: HashMap::new(),
                parent: None,
            },
        );
        FileSystem {
            nodes: h,
            fid_counter: 1,
        }
    }

    fn from(s: &str) -> FileSystem {
        let mut fs = FileSystem::new();

        let mut curr_directory: FileId = 0;

        for line in s.trim().split('\n') {
            let tokens = line.split_whitespace().collect::<Vec<_>>();

            match tokens[0] {
                "$" => {
                    if tokens[1] == "cd" {
                        let file_node = fs.get_node(curr_directory);
                        match tokens[2] {
                            ".." => curr_directory = file_node.parent.unwrap(),
                            "/" => curr_directory = 0,
                            subdirectory => {
                                // check if child exists and if so, update curr_directory pointer
                                curr_directory = *file_node.children.get(subdirectory).unwrap()
                            }
                        }
                    } else if tokens[1] == "ls" {
                    } else {
                        panic!("Unknown command: {}", tokens[1]);
                    }
                }
                "dir" => fs.add_node(tokens[1], 0, curr_directory),
                s => {
                    let file_size = s.parse::<usize>().unwrap();
                    fs.add_node(tokens[1], file_size, curr_directory);
                }
            }
        }

        fs
    }

    fn add_node(&mut self, name: &str, size: usize, parent: FileId) {
        let node_fid = self.fid_counter;
        let node = FileNode {
            fid: node_fid,
            name: name.to_string(),
            children: HashMap::new(),
            parent: Some(parent),
            size,
        };
        self.nodes.insert(node_fid, node);
        let parent_node = self.nodes.get_mut(&parent).unwrap();
        parent_node.children.insert(name.to_string(), node_fid);
        self.fid_counter += 1;
    }

    fn get_node(&self, file_id: FileId) -> &FileNode {
        self.nodes.get(&file_id).unwrap()
    }

    fn size(&self, file_id: FileId) -> usize {
        let mut sum = 0;
        let mut stack = vec![file_id];

        while let Some(fid) = stack.pop() {
            let node = self.get_node(fid);
            sum += node.size;
            for child_fid in node.children.values() {
                stack.push(*child_fid);
            }
        }

        sum
    }

    fn all_sizes(&self) -> Vec<(String, usize)> {
        let mut res: Vec<(String, usize)> = vec![];
        for (fid, node) in &self.nodes {
            if !node.children.is_empty() {
                res.push((node.name.clone(), self.size(*fid)));
            }
        }
        res
    }
}

struct FileNode {
    fid: FileId,
    name: String,
    size: usize,
    children: HashMap<String, FileId>,
    parent: Option<FileId>,
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let fs = FileSystem::from(&input);

        let sum: usize = fs
            .all_sizes()
            .iter()
            .map(|item| item.1)
            .filter(|item| *item <= 100_000)
            .sum();

        println!("{}", sum);
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let fs = FileSystem::from(&input);

        let total_space: usize = 70_000_000;
        let needed_space: usize = 30_000_000;
        let used_space = fs.size(0);
        let free_space = total_space - used_space;

        let need_to_free = needed_space - free_space;

        let to_delete = fs
            .all_sizes()
            .iter()
            .map(|item| item.1)
            .filter(|size| *size >= need_to_free)
            .min()
            .unwrap();

        println!("{}", to_delete);
    }
}
