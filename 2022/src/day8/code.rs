use crate::Solution;
use std::{collections::HashSet, fs};

pub struct Day {
    pub input_path: String,
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(self.input_path.replace("input", "test")).unwrap();

        let mut grid = vec![];
        let lines = input.trim().split('\n');
        for line in lines {
            grid.push(
                line.chars()
                    .map(|c| c.to_string().parse::<u32>().unwrap())
                    .collect::<Vec<_>>(),
            )
        }

        let mut visible = HashSet::new();

        // left pass
        for (r, row) in grid.iter().enumerate() {
            let mut max = None;
            for (c, tree) in row.iter().enumerate() {
                if max.is_none() || tree > max.unwrap() {
                    visible.insert((r, c));
                    max = Some(tree);
                }
            }
        }

        // right pass
        for (r, row) in grid.iter().enumerate() {
            let mut max = None;
            for (c, tree) in row.iter().enumerate().rev() {
                if max.is_none() || tree > max.unwrap() {
                    visible.insert((r, c));
                    max = Some(tree);
                }
            }
        }

        // top pass
        for c in 0..grid[0].len() {
            let mut max = None;
            for (r, row) in grid.iter().enumerate() {
                let tree = row[c];
                if max.is_none() || tree > max.unwrap() {
                    visible.insert((r, c));
                    max = Some(tree);
                }
            }
        }

        // bottom pass
        for c in 0..grid[0].len() {
            let mut max = None;
            for (r, row) in grid.iter().enumerate().rev() {
                let tree = row[c];
                if max.is_none() || tree > max.unwrap() {
                    visible.insert((r, c));
                    max = Some(tree);
                }
            }
        }

        // let mut s = visible.iter().collect::<Vec<_>>();
        // s.sort();

        // println!("Part 1...");
        // println!("{}", input);
        // println!("{:?}", grid);
        println!("{:?}", visible.len());
        // println!("{:?}", s);
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(self.input_path.replace("input", "test")).unwrap();

        let mut grid = vec![];
        let lines = input.trim().split('\n');
        for line in lines {
            grid.push(
                line.chars()
                    .map(|c| c.to_string().parse::<u32>().unwrap())
                    .collect::<Vec<_>>(),
            )
        }

        let mut max = 0;
        for (r, row) in grid.iter().enumerate() {
            for (c, tree) in row.iter().enumerate() {
                let mut left = 0;
                for c2 in (0..c).rev() {
                    left += 1;
                    if grid[r][c2] >= *tree {
                        break;
                    }
                }

                let mut right = 0;
                for c2 in c + 1..row.len() {
                    right += 1;
                    if grid[r][c2] >= *tree {
                        break;
                    }
                }

                let mut up = 0;
                for r2 in (0..r).rev() {
                    up += 1;
                    if grid[r2][c] >= *tree {
                        break;
                    }
                }

                let mut down = 0;
                for r2 in r + 1..grid.len() {
                    down += 1;
                    if grid[r2][c] >= *tree {
                        break;
                    }
                }

                max = max.max(up * right * down * left);
            }
        }

        println!("Part 2...");
        println!("{}", max);
    }
}
