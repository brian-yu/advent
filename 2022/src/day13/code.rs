use crate::Solution;
use std::{cmp::Ordering, fmt, fs, ops::Index};

pub struct Day {
    pub input_path: String,
}

#[derive(Debug, Clone)]
enum Datum {
    Integer(u32),
    List(Vec<Datum>),
}

#[derive(Debug)]
enum Token {
    Open,
    Item(Datum),
}

impl Datum {
    fn from(s: &str) -> Option<Datum> {
        let chars: Vec<char> = s.chars().collect();

        if chars.len() == 1 {
            return Some(Datum::Integer(s.parse().unwrap()));
        }

        let mut stack = Vec::new();
        let mut curr_digit = Vec::new();
        for char in chars {
            match char {
                '[' => stack.push(Token::Open),
                ']' => {
                    if !curr_digit.is_empty() {
                        stack.push(Token::Item(Datum::Integer(
                            curr_digit.iter().collect::<String>().parse().unwrap(),
                        )));
                        curr_digit.clear();
                    }

                    let mut v = vec![];
                    while let Some(c) = stack.pop() {
                        match c {
                            Token::Open => break,
                            Token::Item(datum) => v.push(datum),
                        }
                    }
                    v.reverse();
                    stack.push(Token::Item(Datum::List(v)))
                }
                ',' => {
                    if !curr_digit.is_empty() {
                        stack.push(Token::Item(Datum::Integer(
                            curr_digit.iter().collect::<String>().parse().unwrap(),
                        )));
                        curr_digit.clear();
                    }
                }
                c => {
                    curr_digit.push(c);
                }
            }
        }

        if let Some(Token::Item(datum)) = stack.pop() {
            return Some(datum);
        }

        None
    }
}

impl Ord for Datum {
    fn cmp(&self, right: &Datum) -> Ordering {
        match (self, right) {
            (Datum::Integer(l), Datum::Integer(r)) => l.cmp(r),
            (Datum::List(l), Datum::List(r)) => {
                let mut l_iter = l.iter();
                let mut r_iter = r.iter();
                loop {
                    match (l_iter.next(), r_iter.next()) {
                        (Some(ld), Some(lr)) => match ld.cmp(lr) {
                            Ordering::Less => return Ordering::Less,
                            Ordering::Greater => return Ordering::Greater,
                            Ordering::Equal => (),
                        },
                        (None, Some(_)) => return Ordering::Less,
                        (Some(_), None) => return Ordering::Greater,
                        (None, None) => return Ordering::Equal,
                    }
                }
            }
            (Datum::Integer(l), Datum::List(_)) => Datum::List(vec![Datum::Integer(*l)]).cmp(right),
            (Datum::List(_), Datum::Integer(r)) => self.cmp(&Datum::List(vec![Datum::Integer(*r)])),
        }
    }
}

impl PartialOrd for Datum {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Datum {
    fn eq(&self, other: &Self) -> bool {
        self.cmp(other) == Ordering::Equal
    }
}

impl Eq for Datum {}

impl fmt::Display for Datum {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let mut tokens = vec![];
        match &self {
            Datum::Integer(i) => tokens.push(format!("{}", i)),
            Datum::List(v) => {
                let items: Vec<String> = v.iter().map(|d| d.to_string()).collect();
                tokens.push(format!("[{}]", items.join(",")))
            }
        }

        write!(f, "{}", tokens.join(""))
    }
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let mut result = 0;
        for (idx, pair_s) in input.trim().split("\n\n").enumerate() {
            let (left_s, right_s) = pair_s.split_once('\n').unwrap();
            let left = Datum::from(left_s).unwrap();
            let right = Datum::from(right_s).unwrap();

            if left.cmp(&right) == Ordering::Less {
                result += idx + 1
            }
        }

        println!("{}", result);
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let mut datums: Vec<Datum> = input.split_whitespace().filter_map(Datum::from).collect();

        let marker_1 = Datum::from("[[2]]").unwrap();
        let marker_2 = Datum::from("[[6]]").unwrap();

        datums.push(marker_1.clone());
        datums.push(marker_2.clone());

        datums.sort();

        let index_1 = datums.iter().position(|r| *r == marker_1).unwrap() + 1;
        let index_2 = datums.iter().position(|r| *r == marker_2).unwrap() + 1;

        println!("{:?}", index_1 * index_2);
    }
}
