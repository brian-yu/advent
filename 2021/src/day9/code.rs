use crate::Solution;
use std::{collections::HashSet, fs};

pub struct Day {
    pub input_path: String,
}

struct Grid {
    squares: Vec<Vec<u8>>,
}

impl Grid {
    fn new(input: Vec<&str>) -> Grid {
        let mut result = Vec::new();
        for line in input {
            result.push(
                line.chars()
                    .map(|item| item.to_string().parse::<u8>().unwrap())
                    .collect(),
            );
        }

        Grid { squares: result }
    }

    fn get_neighbor_locations(&self, r: usize, c: usize) -> Vec<Location> {
        let mut neighbors = vec![];
        if r > 0 {
            neighbors.push(Location { r: r - 1, c });
        }
        if r + 1 < self.squares.len() {
            neighbors.push(Location { r: r + 1, c });
        }
        if c > 0 {
            neighbors.push(Location { c: c - 1, r });
        }
        if c + 1 < self.squares[0].len() {
            neighbors.push(Location { c: c + 1, r });
        }

        neighbors
    }

    fn get_neighbors(&self, r: usize, c: usize) -> Vec<u8> {
        self.get_neighbor_locations(r, c)
            .iter()
            .map(|loc| self.squares[loc.r][loc.c])
            .collect()
    }

    fn is_lowest_of_neighbors(&self, r: usize, c: usize) -> bool {
        let height = self.squares[r][c];
        for neighbor in self.get_neighbors(r, c) {
            if height >= neighbor {
                return false;
            }
        }

        true
    }

    fn find_low_points(&self) -> Vec<Location> {
        let mut low_points = vec![];

        for (r, row) in self.squares.iter().enumerate() {
            for c in 0..row.len() {
                if self.is_lowest_of_neighbors(r, c) {
                    low_points.push(Location { r, c })
                }
            }
        }

        low_points
    }

    fn find_basin_size(&self, r: usize, c: usize) -> i32 {
        let mut size = 0;
        let mut candidates = vec![Location { r, c }];
        let mut visited = HashSet::new();
        while let Some(location) = candidates.pop() {
            if visited.contains(&location) {
                continue;
            }

            visited.insert(location.clone());
            size += 1;

            let height = self.squares[location.r][location.c];

            for neighbor in self.get_neighbor_locations(location.r, location.c) {
                let neighbor_height = self.squares[neighbor.r][neighbor.c];
                if !visited.contains(&neighbor) && neighbor_height >= height && neighbor_height != 9
                {
                    candidates.push(neighbor);
                }
            }
        }

        size
    }
}

#[derive(Hash, PartialEq, Eq, Clone, Debug)]
struct Location {
    r: usize,
    c: usize,
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(self.input_path.replace("input", "test")).unwrap();

        let grid = Grid::new(input.trim().split('\n').collect());

        let mut risk: u32 = 0;

        for low_point in grid.find_low_points() {
            let height = grid.squares[low_point.r][low_point.c];
            risk += height as u32 + 1;
        }

        println!("{}", risk);
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(self.input_path.replace("input", "test")).unwrap();

        let grid = Grid::new(input.trim().split('\n').collect());

        let mut basin_sizes: Vec<i32> = grid
            .find_low_points()
            .iter()
            .map(|loc| grid.find_basin_size(loc.r, loc.c))
            .collect();

        basin_sizes.sort_by(|a, b| b.cmp(a));

        println!("{}", basin_sizes[..3].iter().product::<i32>());
    }
}
