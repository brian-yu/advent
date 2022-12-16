use crate::Solution;
use std::collections::hash_map::Entry::Vacant;
use std::{
    collections::{HashMap, VecDeque},
    fs,
};

pub struct Day {
    pub input_path: String,
}

struct Grid {
    squares: Vec<Vec<char>>,
}

impl Grid {
    fn new(s: &str) -> Grid {
        Grid {
            squares: s
                .trim()
                .split('\n')
                .map(|line| line.chars().collect())
                .collect(),
        }
    }

    fn shortest_path(&self, start: (usize, usize)) -> Option<u32> {
        let mut q: VecDeque<(usize, usize)> = VecDeque::from([start]);
        let mut visited = HashMap::new();

        let mut steps = 0;

        while let Some(pos) = q.pop_front() {
            if self.is_end(pos) {
                let mut p = pos;
                while let Some(&parent) = visited.get(&p) {
                    if p == start {
                        break;
                    }
                    p = parent;
                    steps += 1;
                }

                return Some(steps);
            }

            for neighbor in self.traversable_neighbors(pos) {
                if let Vacant(e) = visited.entry(neighbor) {
                    e.insert(pos);
                    q.push_back(neighbor)
                }
            }
        }

        None
    }

    fn find_start(&self) -> (usize, usize) {
        for (r, row) in self.squares.iter().enumerate() {
            for (c, &char) in row.iter().enumerate() {
                if char == 'S' {
                    return (r, c);
                }
            }
        }
        (0, 0)
    }

    fn is_end(&self, pos: (usize, usize)) -> bool {
        self.squares[pos.0][pos.1] == 'E'
    }

    fn height(&self, pos: (usize, usize)) -> u32 {
        let char = match self.squares[pos.0][pos.1] {
            'E' => 'z',
            'S' => 'a',
            c => c,
        };

        char as u32 - ('a' as u32) + 1
    }

    fn traversable_neighbors(&self, pos: (usize, usize)) -> Vec<(usize, usize)> {
        let mut neighbors = vec![];

        let (r, c) = pos;

        if r > 0 {
            neighbors.push((r - 1, c));
        }
        if r + 1 < self.squares.len() {
            neighbors.push((r + 1, c));
        }
        if c > 0 {
            neighbors.push((r, c - 1));
        }
        if c + 1 < self.squares[r].len() {
            neighbors.push((r, c + 1));
        }

        neighbors
            .into_iter()
            .filter(|n_pos| self.height(*n_pos) <= self.height(pos) + 1)
            .collect()
    }

    fn low_positions(&self) -> Vec<(usize, usize)> {
        let mut positions = vec![];
        for (r, row) in self.squares.iter().enumerate() {
            for (c, &char) in row.iter().enumerate() {
                if char == 'a' {
                    positions.push((r, c));
                }
            }
        }
        positions
    }
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let grid = Grid::new(&input);

        println!("{:?}", grid.shortest_path(grid.find_start()));
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let grid = Grid::new(&input);

        println!(
            "{}",
            grid.low_positions()
                .iter()
                .filter_map(|&pos| grid.shortest_path(pos))
                .min()
                .unwrap()
        );
    }
}
