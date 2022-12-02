use crate::Solution;
use std::{
    collections::{HashMap, HashSet},
    fs,
};

pub struct Day {
    pub input_path: String,
}

struct Graph<'a> {
    hash: HashMap<&'a str, HashSet<&'a str>>,
}

impl Graph<'_> {
    fn new<'a, I>(edges: I) -> Graph<'a>
    where
        I: Iterator<Item = &'a str>,
    {
        let mut hash: HashMap<&'a str, HashSet<&str>> = HashMap::new();

        for edge in edges {
            let (source, target) = edge.split_once('-').unwrap();
            if !hash.contains_key(source) {
                hash.insert(source, HashSet::new());
            }
            if !hash.contains_key(target) {
                hash.insert(target, HashSet::new());
            }
            {
                let source_neighbors = hash.get_mut(source).unwrap();
                source_neighbors.insert(target);
            }
            let target_neighbors = hash.get_mut(target).unwrap();
            target_neighbors.insert(source);
        }

        Graph { hash }
    }

    fn count_paths(&self) -> usize {
        let mut count = 0;
        let mut stack = vec![("start", HashSet::new(), vec![])];

        while let Some((v, mut visited, mut path)) = stack.pop() {
            if visited.contains(v) {
                continue;
            }

            path.push(v);

            if v == "end" {
                count += 1;
            }

            if v == v.to_lowercase() {
                visited.insert(v);
            }

            for neighbor in self.hash.get(v).unwrap() {
                stack.push((neighbor, visited.clone(), path.clone()));
            }
        }

        count
    }

    fn count_paths_visiting_a_cave_twice(&self) -> usize {
        let mut count = 0;

        let small_caves = self
            .hash
            .keys()
            .filter(|k| **k == k.to_lowercase() && **k != "start" && **k != "end");

        for double_visited_cave in small_caves {
            let mut stack = vec![("start", HashSet::new(), 0)];

            while let Some((v, mut visited, mut double_visited_cave_visits)) = stack.pop() {
                if (v != *double_visited_cave && visited.contains(v))
                    || (v == *double_visited_cave && double_visited_cave_visits == 2)
                {
                    continue;
                }

                if v == *double_visited_cave {
                    double_visited_cave_visits += 1;
                }

                if v == "end" && double_visited_cave_visits == 2 {
                    count += 1;
                }

                if v == v.to_lowercase() {
                    visited.insert(v);
                }

                for neighbor in self.hash.get(v).unwrap() {
                    stack.push((neighbor, visited.clone(), double_visited_cave_visits));
                }
            }
        }

        count
    }
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(self.input_path.replace("input", "test")).unwrap();

        let graph = Graph::new(input.trim().split('\n'));
        // println!("{:?}", graph.hash);
        println!("{:?}", graph.count_paths());
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(self.input_path.replace("input", "test")).unwrap();

        let graph = Graph::new(input.trim().split('\n'));
        println!(
            "{:?}",
            graph.count_paths() + graph.count_paths_visiting_a_cave_twice()
        );
    }
}
