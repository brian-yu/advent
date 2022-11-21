use std::fs;

use crate::Solution;

pub struct Day {
    pub input_path: String,
}

type Unit = u32;

#[derive(Debug)]
#[derive(Clone)]
#[derive(Copy)]
#[derive(PartialEq)]
struct Position {
    x: Unit,
    y: Unit,
}

impl Position {
    fn new(s: &str) -> Position {
        let (x, y) = s.split_once(",").unwrap();
        Position { x: x.parse().unwrap(), y: y.parse().unwrap() }
    }

    fn translate(&self, dx: i32, dy: i32) -> Position {
        Position {
            x: (self.x as i32 + dx) as Unit,
            y: (self.y as i32 + dy) as Unit,
        }
    }
}

#[derive(Debug)]
#[derive(Clone)]
struct Line {
    from: Position,
    to: Position,
}

impl Line {
    fn new(s: &str) -> Line {
        let (a, b) = s.split_once(" -> ").unwrap();
        Line {from: Position::new(a), to: Position::new(b)}
    }

    fn is_horizontal(&self) -> bool {
        self.from.x == self.to.x
    }

    fn is_vertical(&self) -> bool {
        self.from.y == self.to.y
    }

    fn gradient(&self) -> (i32, i32) {
        let x_grad = self.to.x as i32 - self.from.x as i32;
        let y_grad = self.to.y as i32 - self.from.y as i32;
        
        (x_grad.signum(), y_grad.signum())
    }

    fn iter(&self) -> LineIter {
        LineIter::new(self)
    }
}
impl IntoIterator for Line {
    type Item = Position;
    type IntoIter = LineIter;

    fn into_iter(self) -> Self::IntoIter {
        self.iter()
    }
}

struct LineIter {
    line: Line,
    curr: Option<Position>,
    next: Option<Position>,
}

impl LineIter {
    fn new(line: &Line) -> LineIter {
        let grad = line.gradient();

        LineIter {
            curr: Some(line.from),
            next: Some(line.from.translate(grad.0, grad.1)),
            line: line.clone()
        }
    }
}

impl Iterator for LineIter {
    type Item = Position;

    fn next(&mut self) -> Option<Position> {
        let current = self.curr;

        let grad = self.line.gradient();

        self.curr = self.next;

        if let Some(curr) = self.curr {
            self.next = if curr == self.line.to {
                None
            } else {
                Some(curr.translate(grad.0, grad.1))
            };
        }

        current
    }
}

impl Solution for Day {
    fn part_1(&self) -> () {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let mut lines = Vec::new();

        for line in input.trim().split("\n") {
            let l = Line::new(line); 
            lines.push(l);
        }
        

        let (max_x, max_y) = lines.iter().fold((0, 0), |acc, item| {
            (
                acc.0.max(item.from.x).max(item.to.x),
                acc.1.max(item.from.y).max(item.to.y)
            )            
        });

        let mut grid = vec![vec![0; (max_y + 1) as usize]; (max_x + 1) as usize];

        for line in lines {
            if !(line.is_horizontal() || line.is_vertical()) {
                continue;
            }
            
            for position in line {
                grid[position.x as usize][position.y as usize] += 1
            }
        }

        let mut hotspots = 0;
        for row in grid {
            for intersections in row {
                if intersections >= 2 {
                    hotspots += 1
                }
            }
        }

        println!("Part 1... {}", hotspots);
    }

    fn part_2(&self) -> () {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(&self.input_path.replace("input", "test")).unwrap();

        let mut lines = Vec::new();

        for line in input.trim().split("\n") {
            let l = Line::new(line); 
            lines.push(l);
        }
        

        let (max_x, max_y) = lines.iter().fold((0, 0), |acc, item| {
            (
                acc.0.max(item.from.x).max(item.to.x),
                acc.1.max(item.from.y).max(item.to.y)
            )            
        });

        let mut grid = vec![vec![0; (max_y + 1) as usize]; (max_x + 1) as usize];

        for line in lines {
            for position in line {
                grid[position.x as usize][position.y as usize] += 1
            }
        }

        let mut hotspots = 0;
        for row in grid {
            for intersections in row {
                if intersections >= 2 {
                    hotspots += 1
                }
            }
        }

        println!("{}", hotspots);
    }
}

