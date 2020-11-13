from dis import dis


dis(compile("(10, 'abc')", '', 'eval'))

dis(compile("[10, 'abc']", '', 'eval'))