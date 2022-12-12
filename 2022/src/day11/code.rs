use num_bigint::BigUint;

use crate::Solution;
use std::{
    collections::VecDeque,
    fs,
    ops::{AddAssign, DivAssign, MulAssign},
};

pub struct Day {
    pub input_path: String,
}

struct Monkey {
    items: VecDeque<BigUint>,
    op: Box<dyn Fn(BigUint) -> BigUint>,
    test: Box<dyn Fn(&BigUint) -> usize>,
}

impl Monkey {
    fn from(s: &str) -> Monkey {
        let lines: Vec<&str> = s.split('\n').collect();
        let (_, items_str) = lines[1].split_once(": ").unwrap();
        let (_, op_str) = lines[2].split_once(" = ").unwrap();

        let divisor: usize = lines[3].split_whitespace().last().unwrap().parse().unwrap();
        let if_true: usize = lines[4].split_whitespace().last().unwrap().parse().unwrap();
        let if_false: usize = lines[5].split_whitespace().last().unwrap().parse().unwrap();
        let test: Box<dyn Fn(&BigUint) -> usize> = Box::new(move |x| {
            if x % BigUint::from(divisor) == BigUint::from(0_u8) {
                if_true
            } else {
                if_false
            }
        });

        let items = items_str.split(", ").map(|i| i.parse().unwrap()).collect();

        let op_tokens: Vec<_> = op_str.split_whitespace().collect();
        let op: Box<dyn Fn(BigUint) -> BigUint> = match op_tokens[1] {
            "*" => match op_tokens[2] {
                "old" => Box::new(|x| &x * &x),
                arg => {
                    let op_arg = arg.parse::<BigUint>().unwrap();
                    Box::new(move |x| &x * &op_arg)
                }
            },
            "+" => {
                let op_arg = op_tokens[2].parse::<BigUint>().unwrap();
                Box::new(move |x| &x + &op_arg)
            }
            _ => panic!("Invalid operation: {op_str}"),
        };

        Monkey { items, op, test }
    }
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(self.input_path.replace("input", "test")).unwrap();

        let mut monkeys: Vec<Monkey> = input.trim().split("\n\n").map(Monkey::from).collect();
        let mut inspections: Vec<u32> = monkeys.iter().map(|_| 0).collect();

        for _round in 0..20 {
            for idx in 0..monkeys.len() {
                let throws = {
                    let mut throws: Vec<(usize, BigUint)> = vec![];
                    let monkey = &mut monkeys[idx];
                    while let Some(item) = monkey.items.pop_front() {
                        inspections[idx] += 1;

                        let worry = (monkey.op)(item) / (3_u8);

                        // let worry = (monkey.op)(item)
                        let new_monkey = (monkey.test)(&worry);
                        throws.push((new_monkey, worry));
                    }
                    throws
                };

                for (new_monkey, worry) in throws {
                    monkeys[new_monkey].items.push_back(worry);
                }
            }
        }

        inspections.sort();
        println!("{:?}", inspections.iter().rev().take(2).product::<u32>())
    }

    fn part_2(&self) {
        // let input = fs::read_to_string(&self.input_path).unwrap();
        let input = fs::read_to_string(self.input_path.replace("input", "test")).unwrap();

        let mut monkeys: Vec<Monkey> = input.trim().split("\n\n").map(Monkey::from).collect();
        let mut inspections: Vec<u32> = monkeys.iter().map(|_| 0).collect();

        for round in 0..10_000 {
            if round % 100 == 0 {
                println!("Round {}", round);
            }
            for idx in 0..monkeys.len() {
                let throws = {
                    let mut throws: Vec<(usize, BigUint)> = vec![];
                    let monkey = &mut monkeys[idx];
                    while let Some(item) = monkey.items.pop_front() {
                        inspections[idx] += 1;

                        let worry = (monkey.op)(item);

                        // let new_monkey = (monkey.test)(&worry);
                        let new_monkey = (monkey.test)(&worry);
                        throws.push((new_monkey, worry));
                    }
                    throws
                };

                for (new_monkey, worry) in throws {
                    monkeys[new_monkey].items.push_back(worry);
                }
            }
        }

        inspections.sort();
        println!("{:?}", inspections.iter().rev().take(2).product::<u32>())
    }
}
