use crate::Solution;
use std::fs;

pub struct Day {
    pub input_path: String,
}

struct Multistack {
    stacks: Vec<Vec<char>>,
}

impl Multistack {
    fn from_str(s: &str) -> Multistack {
        let num_stacks = s
            .split_whitespace()
            .last()
            .unwrap()
            .parse::<usize>()
            .unwrap();

        let mut stacks = vec![Vec::new(); num_stacks];

        for (i, chunk) in s.chars().array_chunks::<4>().enumerate() {
            if chunk[0] == '[' {
                stacks[i % num_stacks].push(chunk[1]);
            }
        }

        for stack in stacks.iter_mut() {
            stack.reverse();
        }

        Multistack { stacks }
    }

    fn tops(&self) -> String {
        self.stacks
            .iter()
            .map(|stack| stack.last().unwrap())
            .collect()
    }

    fn pop(&mut self, stack: usize, quantity: usize) -> Vec<char> {
        let source_stack = &mut self.stacks[stack];
        source_stack
            .drain(source_stack.len() - quantity..)
            .collect()
    }

    fn push(&mut self, stack: usize, items: Vec<char>) {
        self.stacks[stack].extend(items);
    }
}

struct Instruction {
    quantity: usize,
    source: usize,
    target: usize,
}

fn parse_instructions(s: &str) -> Vec<Instruction> {
    s.trim()
        .split('\n')
        .map(|line| {
            let tokens = line.split_whitespace().collect::<Vec<_>>();
            let quantity = tokens[1].parse::<usize>().unwrap();
            let source = tokens[3].parse::<usize>().unwrap() - 1;
            let target = tokens[5].parse::<usize>().unwrap() - 1;

            Instruction {
                quantity,
                source,
                target,
            }
        })
        .collect()
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let (stacks_str, instructions) = input.split_once("\n\n").unwrap();

        let mut mstack = Multistack::from_str(stacks_str);

        for instruction in parse_instructions(instructions) {
            for _ in 0..instruction.quantity {
                let item = mstack.pop(instruction.source, 1);
                mstack.push(instruction.target, item);
            }
        }

        println!("{}", mstack.tops());
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let (stacks_str, instructions) = input.split_once("\n\n").unwrap();

        let mut mstack = Multistack::from_str(stacks_str);

        for instruction in parse_instructions(instructions) {
            let item = mstack.pop(instruction.source, instruction.quantity);
            mstack.push(instruction.target, item);
        }

        println!("{}", mstack.tops());
    }
}
