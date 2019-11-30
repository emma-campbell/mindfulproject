from . import Demographics

from flask import current_app, request

@bp.route('/users/<id>/demographics', methods=['GET'])
def get_demographics(id):
    '''Return the demographics of the user with {@code id}'''
    return Demographics.query.filter_by(id=id).first()


@bp.route('/users/<id>/demographics', methods=['POST'])
def update_demographics(id):
    '''
    Update the Demographics of a User

    1. First, grab the form from main
    2. Then, return the rendered front end the form
    3. have the user fill it out, grab it, and store it here

    I am not predicting that demographic information will
    accessed heaviliy, so I am placing it in its own table
    indexed by the user id number
    '''
    pass
