
use std::collections::HashMap;
use std::fs;

use crate::Solution;

pub struct Day {
    pub input_path: String,
}

fn most_common_bit_for_idx(numbers: &Vec<&str>, idx: usize) -> char {
    let mut count = (0, 0);
    for number in numbers {
        count = match (*number).chars().nth(idx).unwrap() {
            '0' => (count.0 + 1, count.1),
            '1' => (count.0, count.1 + 1),
            _ => panic!("Unrecognized bit value")
        }
    }

    if count.0 > count.1 {
        '0'
    } else {
        '1'
    }
}

fn find_rating<F>(mut numbers: Vec<&str>, f: F) -> &str where F: Fn(char, char) -> bool {
    for idx in 0..numbers.first().unwrap().len() {
        let mut filtered_numbers = Vec::new();
        let most_common_bit = most_common_bit_for_idx(&numbers, idx);
        for number in numbers {
            if f(number.chars().nth(idx).unwrap(), most_common_bit) {
                filtered_numbers.push(number);
            }
        }
        numbers = filtered_numbers.clone();
        if numbers.len() == 1 {
            break;
        }
    }

    assert!(numbers.len() == 1);

    numbers.first().unwrap()
}

impl Solution for Day {
    fn part_1(&self) -> () {
        let input = fs::read_to_string(&self.input_path).unwrap();
        let numbers = input.trim().split("\n");

        let mut counts: HashMap<usize, (u32, u32)> = HashMap::new();

        for number in numbers {
            for (idx, bit) in number.chars().enumerate() {
                let curr_count = counts.get(&idx).unwrap_or(&(0, 0));
                let count = match bit {
                    '0' => (curr_count.0 + 1, curr_count.1),
                    '1' => (curr_count.0, curr_count.1 + 1),
                    _ => panic!("invalid bit value")
                };
                counts.insert(idx, count);
            }
        }

        let mut gamma_bits = vec![0; counts.len()];
        let mut epsilon_bits = vec![0; counts.len()];
        for (idx, count) in counts.iter() {
            if count.0 > count.1 {
                gamma_bits[*idx] = 0;
                epsilon_bits[*idx] = 1;
            } else {
                gamma_bits[*idx] = 1;
                epsilon_bits[*idx] = 0;
            }
        }

        let gamma_binary = gamma_bits.iter().map(|item| item.to_string()).collect::<Vec<String>>().join("");
        let epsilon_binary = epsilon_bits.iter().map(|item| item.to_string()).collect::<Vec<String>>().join("");

        let gamma = isize::from_str_radix(&gamma_binary, 2).unwrap();
        let epsilon = isize::from_str_radix(&epsilon_binary, 2).unwrap();
        
        println!("{:?} {:?} {:?}", gamma, epsilon, gamma * epsilon)
    }

    fn part_2(&self) -> () {
        let input = fs::read_to_string(&self.input_path).unwrap();
        
        let oxygen_rating_binary = find_rating(input.trim().split("\n").collect(), |a, b| a == b);
        let oxygen_rating = isize::from_str_radix(oxygen_rating_binary, 2).unwrap();

        let co2_rating_binary = find_rating(input.trim().split("\n").collect(), |a, b| a != b);
        let co2_rating = isize::from_str_radix(co2_rating_binary, 2).unwrap();
        
        println!("{:?} {:?} {:?}", oxygen_rating, co2_rating, oxygen_rating*co2_rating);
    }
}

