# -*- coding: utf-8 -*-

from aiida.plugins import CalculationFactory
from aiida.orm import Int
from aiida.engine import run_get_node
from aiida import cmdline

import click


ArithmeticAdd = CalculationFactory('arithmetic.add')

def add_together(i, code):
    x = Int(i)
    builder = ArithmeticAdd.get_builder()
    builder.x = x
    builder.y = x
    builder.code = code
    
    print('Adding {} + {} on computer {}'.format(x.value, x.value, code.computer.label))
    result = run_get_node(builder)
    print('Result {}'.format(result[0]['sum'].value))


@click.command('cli')
@cmdline.utils.decorators.with_dbenv()
@click.option('--add_code', type=cmdline.params.types.CodeParamType())
def main(add_code):
    for i in range(3):
        add_together(i, add_code)

if __name__ == '__main__':
    main()