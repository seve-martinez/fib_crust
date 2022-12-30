use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn say_hello() {
    println!("saying hello from rust!");
}


#[pymodule]
fn fib_crust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(say_hello))?;

    Ok(())
}
