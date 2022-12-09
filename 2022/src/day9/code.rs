use crate::Solution;
use core::panic;
use std::{collections::HashSet, fs};

pub struct Day {
    pub input_path: String,
}

const DIAGONAL_OFFSETS: [(i32, i32); 4] = [(-1, -1), (-1, 1), (1, -1), (1, 1)];

#[derive(Debug, Clone)]
struct Position {
    x: i32,
    y: i32,
}

impl Position {
    fn new(x: i32, y: i32) -> Position {
        Position { x, y }
    }

    fn touching(&self, other: &Position) -> bool {
        let x_dist = self.x.abs_diff(other.x);
        let y_dist = self.y.abs_diff(other.y);

        x_dist <= 1 && y_dist <= 1
    }

    fn to_tuple(&self) -> (i32, i32) {
        (self.x, self.y)
    }
}

fn solve(input: &str, num_knots: usize) -> usize {
    let mut knots = vec![];
    for _ in 0..num_knots {
        knots.push(Position::new(0, 0));
    }

    let mut tail_visited = HashSet::new();
    tail_visited.insert(knots.last().unwrap().to_tuple());

    for line in input.trim().split('\n') {
        let (direction, distance_str) = line.split_once(' ').unwrap();

        let distance: i32 = distance_str.parse().unwrap();

        for _ in 0..distance {
            match direction {
                "U" => knots[0].y += 1,
                "D" => knots[0].y -= 1,
                "R" => knots[0].x += 1,
                "L" => knots[0].x -= 1,
                _ => panic!("Invalid direction: {}", direction),
            }

            for i in 1..knots.len() {
                // TODO: Figure out how to remove this clone.
                let prev_knot = knots[i - 1].clone();
                let mut knot = &mut knots[i];

                if !knot.touching(&prev_knot) {
                    if knot.x == prev_knot.x {
                        knot.y += (prev_knot.y - knot.y).clamp(-1, 1)
                    } else if knot.y == prev_knot.y {
                        knot.x += (prev_knot.x - knot.x).clamp(-1, 1)
                    } else {
                        // must move diagonally
                        for (dx, dy) in DIAGONAL_OFFSETS {
                            if prev_knot.touching(&Position::new(knot.x + dx, knot.y + dy)) {
                                knot.x += dx;
                                knot.y += dy;
                                break;
                            }
                        }
                    }
                }
            }

            tail_visited.insert(knots.last().unwrap().to_tuple());
        }
    }

    tail_visited.len()
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        println!("{}", solve(&input, 2));
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        println!("{}", solve(&input, 10));
    }
}
