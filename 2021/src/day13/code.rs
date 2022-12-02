use crate::Solution;
use std::{
    fmt::{self, Display},
    fs,
};

pub struct Day {
    pub input_path: String,
}

struct Paper {
    grid: Vec<Vec<char>>,
}

impl Paper {
    fn new<'a, I>(lines: I) -> Paper
    where
        I: Iterator<Item = &'a str>,
    {
        let mut max_x = 0;
        let mut max_y = 0;

        let positions = lines
            .map(|line| {
                let (x, y) = line.split_once(',').unwrap();
                (x.parse::<usize>().unwrap(), y.parse::<usize>().unwrap())
            })
            .collect::<Vec<(usize, usize)>>();

        for (x, y) in &positions {
            max_x = (*x).max(max_x);
            max_y = (*y).max(max_y);
        }

        let mut grid = vec![];
        for _ in 0..=max_y {
            grid.push(vec!['.'; max_x + 1]);
        }

        for (x, y) in &positions {
            grid[*y][*x] = '#';
        }

        Paper { grid }
    }

    // fold up with a horizontal crease
    fn fold_y(&mut self, y: usize) {
        let mut new_grid = vec![];
        for r in 0..y {
            new_grid.push(self.grid[r].clone());
        }

        let new_grid_len = new_grid.len();

        for r in y + 1..self.grid.len() {
            let row = &self.grid[r];
            let offset_r = r - (y + 1);
            if offset_r < new_grid.len() {
                for (c, val) in row.iter().enumerate() {
                    if *val == '#' {
                        new_grid[new_grid_len - 1 - offset_r][c] = '#';
                    }
                }
            }
        }

        self.grid = new_grid
    }

    // fold left with a vertical crease
    fn fold_x(&mut self, x: usize) {
        let mut new_grid = vec![];
        for (r, _) in self.grid.iter().enumerate() {
            new_grid.push(vec!['.'; x]);
            for c in 0..x {
                new_grid[r][c] = self.grid[r][c];
            }
        }

        for (r, row) in self.grid.iter().enumerate() {
            for (c, val) in row.iter().enumerate().skip(x + 1) {
                let offset_c = c - (x + 1);
                if *val == '#' {
                    new_grid[r][x - 1 - offset_c] = '#';
                }
            }
        }

        self.grid = new_grid
    }

    fn count_dots(&self) -> usize {
        self.grid
            .iter()
            .map(|row| row.iter().filter(|c| **c == '#').count())
            .sum()
    }
}

impl Display for Paper {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let output = self.grid.iter().map(|row| {
            row.iter()
                .map(|i| i.to_string())
                .collect::<Vec<String>>()
                .join("")
        });
        write!(f, "{}", output.collect::<Vec<String>>().join("\n"))
    }
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(self.input_path.replace("input", "test")).unwrap();

        let (positions, instructions) = input.trim().split_once("\n\n").unwrap();

        let mut paper = Paper::new(positions.split_whitespace());

        let instruction = instructions.trim().split('\n').next().unwrap();

        let tokens = instruction.split_whitespace().collect::<Vec<&str>>();
        let (direction, line_str) = tokens[tokens.len() - 1].split_once('=').unwrap();
        let line = line_str.parse::<usize>().unwrap();
        match direction {
            "x" => paper.fold_x(line),
            "y" => paper.fold_y(line),
            _ => panic!("Could not parse instruction: {}", instruction),
        }
        println!("{}", paper.count_dots());
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(self.input_path.replace("input", "test")).unwrap();

        let (positions, instructions) = input.trim().split_once("\n\n").unwrap();

        let mut paper = Paper::new(positions.split_whitespace());

        for instruction in instructions.trim().split('\n') {
            let tokens = instruction.split_whitespace().collect::<Vec<&str>>();
            let (direction, line_str) = tokens[tokens.len() - 1].split_once('=').unwrap();
            let line = line_str.parse::<usize>().unwrap();
            match direction {
                "x" => paper.fold_x(line),
                "y" => paper.fold_y(line),
                _ => panic!("Could not parse instruction: {}", instruction),
            }
        }

        println!("{}", paper);
    }
}
