use std::{fs, collections::HashMap};
use crate::Solution;

pub struct Day {
    pub input_path: String,
}

const NUM_ROWS: usize = 5;
const NUM_COLS: usize = NUM_ROWS;

#[derive(Debug)]
#[derive(Copy)]
#[derive(Clone)]
struct Square {
    num: u32,
    marked: bool,
}

#[derive(Debug)]
struct Board {
    squares: [[Square; NUM_COLS]; NUM_ROWS],
    positions: HashMap<u32, Vec<(usize, usize)>>,
}

impl Board {
    fn empty() -> Board {
        Board{squares: [[Square{num: 0, marked: false}; NUM_COLS]; NUM_ROWS], positions: HashMap::new()}
    }

    fn read(s: &str) -> Board {
        let mut board = Board::empty();
        for (i, line) in s.split("\n").enumerate() {
            for (j, num_str) in line.split_whitespace().enumerate() {
                let num = num_str.parse().unwrap();
                board.squares[i][j] = Square{marked: false, num};
                if let Some(vec) = board.positions.get_mut(&num) {
                    vec.push((i, j));
                } else {
                    board.positions.insert(num, vec![(i, j)]);
                }
            }

        }
        board
    }

    fn mark(&mut self, num: u32) -> () {
        let positions = match self.positions.get(&num) {
            Some(p) => p,
            None => return,
        };

        for (i, j) in positions {
            self.squares[*i][*j].marked = true;
        }
    }

    fn check(&self) -> bool {
        // rows
        for row in self.squares {
            if row.iter().all(|s| s.marked) {
                return true;
            }
        }

        // cols
        'outer: for c in 0..NUM_COLS {
            for r in 0..NUM_ROWS {
                if !self.squares[r][c].marked {
                    continue 'outer;
                }
            }
            return true
        }

        false
    }

    fn sum_unmarked(&self) -> u32 {
        let mut sum = 0;
        for row in self.squares {
            for square in row {
                if !square.marked {
                    sum += square.num;
                }
            }
        }
        sum
    }
}

impl Solution for Day {
    fn part_1(&self) -> () {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string("src/day4/test.txt").unwrap();
        let mut chunks = input.split("\n\n");

        let drawn_numbers: Vec<u32> = chunks.next().unwrap().split(",").map(|item| item.parse::<u32>().unwrap()).collect();

        let mut boards = Vec::new();

        for board_chunk in chunks {
            println!("----");
            println!("{}", board_chunk);
            boards.push(Board::read(board_chunk));
        }

        println!("{:?}", drawn_numbers);

        for number in drawn_numbers {
            for board in &mut boards {
                board.mark(number);
                if board.check() {
                    println!("found winning board!");
                    println!("number: {}, sum_unmarked: {}, score: {:?}", number, board.sum_unmarked(), number * board.sum_unmarked());
                    return
                }
            }
        }
    }

    fn part_2(&self) -> () {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string("src/day4/test.txt").unwrap();
        let mut chunks = input.split("\n\n");

        let drawn_numbers: Vec<u32> = chunks.next().unwrap().split(",").map(|item| item.parse::<u32>().unwrap()).collect();

        let mut boards = Vec::new();

        for board_chunk in chunks {
            boards.push(Board::read(board_chunk));
        }

        println!("{:?}", drawn_numbers);

        let mut last_winning_board = None;
        let mut winning_board_scores = HashMap::new();
        for number in drawn_numbers{
            let num_boards = boards.len();
            for (idx, board) in boards.iter_mut().enumerate() {
                if winning_board_scores.len() == num_boards {
                    println!("{}", winning_board_scores.get(
                        &last_winning_board.expect("There should be at least 1 winning board")).unwrap());
                    return;
                }
                board.mark(number);
                if board.check() {
                    last_winning_board = Some(idx);
                    winning_board_scores.insert(idx, number * board.sum_unmarked());
                }
            }
        }

        

    }
}

