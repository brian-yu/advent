use crate::Solution;
use std::{
    collections::HashSet,
    fmt::{self, Display},
    fs,
};

pub struct Day {
    pub input_path: String,
}

struct Grid {
    squares: Vec<Vec<u8>>,
}

impl Grid {
    // fn new(vec: Iterator<&str>) -> Grid {
    fn new<'a, I>(lines: I) -> Grid
    where
        I: Iterator<Item = &'a str>,
    {
        let mut squares = vec![];
        for line in lines {
            squares.push(
                line.chars()
                    .map(|i| i.to_string().parse::<u8>().unwrap())
                    .collect(),
            )
        }
        Grid { squares }
    }

    fn add_one(&mut self) {
        for row in self.squares.iter_mut() {
            for item in row {
                *item += 1;
            }
        }
    }

    fn neighbors(&self, r: usize, c: usize) -> Vec<(usize, usize)> {
        let mut v = vec![];
        if r > 0 {
            if c > 0 {
                v.push((r - 1, c - 1));
            }
            v.push((r - 1, c));
            if c < self.squares.len() - 1 {
                v.push((r - 1, c + 1));
            }
        }
        if r < self.squares.len() - 1 {
            if c > 0 {
                v.push((r + 1, c - 1));
            }
            v.push((r + 1, c));
            if c < self.squares.len() - 1 {
                v.push((r + 1, c + 1));
            }
        }
        if c > 0 {
            v.push((r, c - 1));
        }
        if c < self.squares[0].len() - 1 {
            v.push((r, c + 1));
        }
        v
    }

    fn flash(&mut self) -> HashSet<(usize, usize)> {
        let mut stack = vec![];
        for (r, row) in self.squares.iter().enumerate() {
            for (c, item) in row.iter().enumerate() {
                if *item > 9 {
                    stack.push((r, c));
                }
            }
        }

        let mut flashed = HashSet::new();
        while let Some((r, c)) = stack.pop() {
            if flashed.contains(&(r, c)) {
                continue;
            }

            flashed.insert((r, c));

            for (nr, nc) in self.neighbors(r, c) {
                self.squares[nr][nc] += 1;
                if self.squares[nr][nc] > 9 {
                    stack.push((nr, nc));
                }
            }
        }

        flashed
    }

    fn is_synced_flash(&self) -> bool {
        self.squares
            .iter()
            .map(|row| row.iter().all(|e| *e == 0))
            .all(|e| e)
    }

    fn run_step(&mut self) -> usize {
        self.add_one();

        let flashed = self.flash();

        for (r, c) in &flashed {
            self.squares[*r][*c] = 0;
        }

        flashed.len()
    }
}

impl Display for Grid {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let output = self.squares.iter().map(|row| {
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

        let mut grid = Grid::new(input.trim().split('\n'));

        let mut flashes = 0;
        for _ in 0..100 {
            flashes += grid.run_step();
        }

        println!("{}", flashes);
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(self.input_path.replace("input", "test")).unwrap();

        let mut grid = Grid::new(input.trim().split('\n'));

        let mut step = 0;
        while !grid.is_synced_flash() {
            grid.run_step();
            step += 1;
        }
        println!("{}", step);
    }
}
