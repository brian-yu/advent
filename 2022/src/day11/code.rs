use rug::Integer;

use crate::Solution;
use std::{
    collections::VecDeque,
    fs,
    ops::{AddAssign, DivAssign, MulAssign},
};

pub struct Day {
    pub input_path: String,
}

#[derive(Clone)]
struct Item {
    worry: usize,
    dividing_factor: usize,
}

enum Op {
    Addition(Operand),
    Multiplication(Operand),
}

enum Operand {
    Old,
    Val(Integer),
}

struct Monkey {
    items: VecDeque<Integer>,
    op: Box<dyn Fn(Integer) -> Integer>,
    test: Box<dyn Fn(Integer) -> (usize, Integer)>,
    op_type: Op,
    divisor: usize,
    if_true: usize,
    if_false: usize,
    // operand: Operand,
}

impl Monkey {
    fn from(s: &str) -> Monkey {
        let lines: Vec<&str> = s.split('\n').collect();
        let (_, items_str) = lines[1].split_once(": ").unwrap();
        let (_, op_str) = lines[2].split_once(" = ").unwrap();

        let divisor: usize = lines[3].split_whitespace().last().unwrap().parse().unwrap();
        let if_true: usize = lines[4].split_whitespace().last().unwrap().parse().unwrap();
        let if_false: usize = lines[5].split_whitespace().last().unwrap().parse().unwrap();
        let test = Box::new(move |x| {
            if &x % Integer::from(divisor) == 0 {
                (if_true, x)
            } else {
                (if_false, x)
            }
        });

        let items = items_str.split(", ").map(|i| i.parse().unwrap()).collect();

        let op_tokens: Vec<_> = op_str.split_whitespace().collect();
        let op: Box<dyn Fn(Integer) -> Integer> = match op_tokens[1] {
            "*" => match op_tokens[2] {
                "old" => Box::new(|x| x.square()),
                arg => {
                    let op_arg = arg.parse::<usize>().unwrap();
                    Box::new(move |x| x * op_arg)
                }
            },
            "+" => {
                let op_arg = op_tokens[2].parse::<usize>().unwrap();
                Box::new(move |x| x * op_arg)
            }
            _ => panic!("Invalid operation: {op_str}"),
        };

        let operand = match op_tokens[2] {
            "old" => Operand::Old,
            arg => Operand::Val(Integer::from(arg.parse::<usize>().unwrap())),
        };

        let op_type = match op_tokens[1] {
            "*" => Op::Multiplication(operand),
            "+" => Op::Addition(operand),
            _ => panic!("Invalid operation: {op_str}"),
        };

        Monkey {
            items,
            op,
            test,
            op_type,
            divisor,
            if_true,
            if_false,
        }
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
                    let mut throws: Vec<(usize, Integer)> = vec![];
                    let monkey = &mut monkeys[idx];
                    while let Some(item) = monkey.items.pop_front() {
                        inspections[idx] += 1;

                        let worry = (monkey.op)(item) / 3;
                        let (new_monkey, worry) = (monkey.test)(worry);
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

        // for round in 0..10_000 {
        for round in 0..20 {
            if round % 100 == 0 {
                println!("Round {round}");
            }
            for idx in 0..monkeys.len() {
                let throws = {
                    let mut throws: Vec<(usize, Integer)> = vec![];
                    let monkey = &mut monkeys[idx];
                    while let Some(item) = monkey.items.pop_front() {
                        inspections[idx] += 1;

                        // let worry = (monkey.op)(item);

                        let worry = match &monkey.op_type {
                            Op::Addition(arg) => match arg {
                                Operand::Old => panic!("oops"),
                                Operand::Val(val) => item + val,
                            },
                            Op::Multiplication(arg) => match arg {
                                Operand::Old => item.square(),
                                Operand::Val(val) => item * val,
                            },
                        };

                        let worry: Integer = worry / 3;

                        let new_monkey = if worry.clone() % monkey.divisor == 0 {
                            monkey.if_true
                        } else {
                            monkey.if_false
                        };

                        // let (new_monkey, worry) = (monkey.test)(worry);
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
