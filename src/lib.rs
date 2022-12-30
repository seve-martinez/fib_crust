mod fib_calcs;

use pyo3::prelude::*;
use pyo3::wrap_pyfunction;


use fib_calcs::fib_number::__pyo3_get_function_fibonacci_number;
use fib_calcs::fib_numbers::__pyo3_get_function_fibonacci_numbers;

// pub mod fib_numbers;

#[pyfunction]
fn say_hello() {
    println!("saying hello from rust!");
}


#[pymodule]
fn fib_crust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(say_hello))?;
    m.add_wrapped(wrap_pyfunction!(fibonacci_number))?;
    m.add_wrapped(wrap_pyfunction!(fibonacci_numbers))?;

    Ok(())
}
