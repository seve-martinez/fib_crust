use pyo3::prelude::pyfunction;

#[pyfunction]
pub fn fibonacci_number(number: i32) -> u64 {
    if n < 0 {
        panic!("{} cannot be negative", n);
    }

    match n {
        0 => panic!("Cannot use zero as an argument"),
        1 | 2 => 1,
        _ => fibonacci_number(n - 1) + fibonacci_number(n - 2)
    }
}
