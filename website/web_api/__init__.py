



# from flask import Blueprint, jsonify, request
# from website.web_models import Show, Venue, User
# from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
# from website import db
#
# api_bp = Blueprint('web_api', __name__)
#
# # from website.web_api import shows, errors, tokens
#
#
# @api_bp.route('/api/shows')
# def shows():
#     shows = Show.query.all()
#     if not shows:
#         return jsonify({})
#
#     lis = [show.to_dict() for show in shows]
#
#     return jsonify(lis)
#
#
# @api_bp.route('/api/show/<int:id>')
# def get_show(id):
#     show = Show.query.filter_by(id=id).first()
#     if not show:
#         return jsonify({})
#     return jsonify(show.to_dict())
#
#
# @api_bp.route('/api/venues')
# def venues():
#     venues = Venue.query.all()
#     if not venues:
#         return jsonify({})
#     lis = [venue.to_dict() for venue in venues]
#     return jsonify(lis)
#
#
# @api_bp.route('/api/venue/<int:id>')
# def get_venue(id):
#     venue = Venue.query.filter_by(id=id).first()
#     if not venue:
#         return jsonify({})
#     return jsonify(venue.to_dict())
#
#
# @api_bp.route('/api/login', methods=['POST'])
# def login():
#     username = request.json.get('username', None)
#     password = request.json.get('password', None)
#     user = User.query.filter_by(username=username, admin=1).first()
#     if not user or not user.password == password:
#         return {'message': 'Invalid username or password'}, 401
#     access_token = create_access_token(identity=user.id)
#     return {'access_token': access_token}, 200
#
#
# @api_bp.route('/api/create-show', methods=['POST'])
# @jwt_required()
# def create_show():
#     current_user_id = get_jwt_identity()
#     if not current_user_id:
#         return {'message': 'Invalid user'}, 401
#     user = User.query.filter_by(id=current_user_id, admin=1).first()
#     if not user or not user.is_authenticated or not user.is_active or not user.is_user:
#         return {'message': 'Unauthorized to create shows'}, 401
#
#     name = request.json.get('name')
#     rating = request.json.get('rating')
#     ticket_price = request.json.get('ticket_price')
#     start_time = request.json.get('start_time')
#     timing = request.json.get('timing')
#     venue_id = request.json.get('venue_id')
#     if not (name and rating and ticket_price and start_time and timing and venue_id):
#         return {'message': 'Values cannot be empty'}, 401
#
#     show = Show(
#         name=name,
#         rating=rating,
#         ticket_price=ticket_price,
#         start_time=start_time,
#         timing=timing,
#         venue_id=venue_id
#     )
#     db.session.add(show)
#     db.session.commit()
#     return {'message': 'Show created successfully'}, 201
#
#
#
# @api_bp.route('/api/create-venue', methods=['POST'])
# @jwt_required()
# def create_venue():
#     current_user_id = get_jwt_identity()
#     if not current_user_id:
#         return {'message': 'Invalid user'}, 401
#     user = User.query.filter_by(id=current_user_id, admin=1).first()
#     if not user or not user.is_authenticated or not user.is_active or not user.is_user:
#         return {'message': 'Unauthorized to create venues'}, 401
#
#     name = request.json.get('name')
#     place = request.json.get('place')
#     capacity = request.json.get('capacity')
#     location = request.json.get('location')
#     admin_id = request.json.get('admin_id')
#
#     if not (name and place and capacity and location and admin_id):
#         return {'message': 'Values cannot be empty'}, 401
#
#     venue = Venue(
#         name=name,
#         place=place,
#         capacity=capacity,
#         location=location,
#         admin_id=admin_id
#     )
#     db.session.add(venue)
#     db.session.commit()
#     return {'message': 'Venue created successfully'}, 201
#
#
# @api_bp.route('/api/update-show/<int:show_id>', methods=['PUT'])
# @jwt_required()
# def update_show(show_id):
#     current_user_id = get_jwt_identity()
#     if not current_user_id:
#         return {'message': 'Invalid user'}, 401
#     user = User.query.filter_by(id=current_user_id, admin=1).first()
#     if not user or not user.is_authenticated or not user.is_active or not user.is_user:
#         return {'message': 'Unauthorized to update shows'}, 401
#
#     show = Show.query.filter_by(id=show_id).first()
#     if not show:
#         return {'message': 'Show not found'}, 404
#
#     name = request.json.get('name', show.name)
#     rating = request.json.get('rating', show.rating)
#     ticket_price = request.json.get('ticket_price', show.ticket_price)
#     start_time = request.json.get('start_time', show.start_time)
#     timing = request.json.get('timing', show.timing)
#     venue_id = request.json.get('venue_id', show.venue_id)
#
#     if not (name and rating and ticket_price and start_time and timing and venue_id):
#         return {'message': 'Values cannot be empty'}, 400
#
#     show.name = name
#     show.rating = rating
#     show.ticket_price = ticket_price
#     show.start_time = start_time
#     show.timing = timing
#     show.venue_id = venue_id
#
#     db.session.commit()
#
#     return {'message': 'Show updated successfully'}, 200
#
#
#
# @api_bp.route('/api/update-venue/<int:venue_id>', methods=['PUT'])
# @jwt_required()
# def update_venue(venue_id):
#     current_user_id = get_jwt_identity()
#     if not current_user_id:
#         return {'message': 'Invalid user'}, 401
#     user = User.query.filter_by(id=current_user_id, admin=1).first()
#     if not user or not user.is_authenticated or not user.is_active or not user.is_user:
#         return {'message': 'Unauthorized to update venues'}, 401
#
#     venue = Venue.query.filter_by(id=venue_id).first()
#     if not venue:
#         return {'message': 'Venue not found'}, 404
#
#     name = request.json.get('name')
#     place = request.json.get('place')
#     capacity = request.json.get('capacity')
#     location = request.json.get('location')
#     admin_id = request.json.get('admin_id')
#
#     if name:
#         venue.name = name
#     if place:
#         venue.place = place
#     if capacity:
#         venue.capacity = capacity
#     if location:
#         venue.location = location
#     if admin_id:
#         venue.admin_id = admin_id
#
#     db.session.commit()
#     return {'message': 'Venue updated successfully'}, 200
#
#
# @api_bp.route('/api/delete-venue/<int:venue_id>', methods=['DELETE'])
# @jwt_required()
# def delete_venue(venue_id):
#     current_user_id = get_jwt_identity()
#     if not current_user_id:
#         return {'message': 'Invalid user'}, 401
#     user = User.query.filter_by(id=current_user_id, admin=1).first()
#     if not user or not user.is_authenticated or not user.is_active or not user.is_user:
#         return {'message': 'Unauthorized to delete venues'}, 401
#
#     venue = Venue.query.filter_by(id=venue_id).first()
#     if not venue:
#         return {'message': 'Venue not found'}, 404
#
#     db.session.delete(venue)
#     db.session.commit()
#     return {'message': 'Venue deleted successfully'}, 200
#
#
# @api_bp.route('/api/delete-show/<int:show_id>', methods=['DELETE'])
# @jwt_required()
# def delete_show(show_id):
#     current_user_id = get_jwt_identity()
#     if not current_user_id:
#         return {'message': 'Invalid user'}, 401
#     user = User.query.filter_by(id=current_user_id, admin=1).first()
#     if not user or not user.is_authenticated or not user.is_active or not user.is_user:
#         return {'message': 'Unauthorized to delete shows'}, 401
#
#     show = Show.query.filter_by(id=show_id).first()
#     if not show:
#         return {'message': 'Show not found'}, 404
#
#     db.session.delete(show)
#     db.session.commit()
#     return {'message': 'Show deleted successfully'}, 200
