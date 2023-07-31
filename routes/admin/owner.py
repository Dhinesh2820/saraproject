from flask import Blueprint, jsonify,request,render_template
from models import Users,db
owner_bp = Blueprint('owner', __name__)


@owner_bp.route('/')
def get_users():
    
    status_param = request.args.get('status')
    if status_param is not None:
        status = int(status_param)
        if status == 1:
            users = db.session.query(Users).filter_by(status=1).all()
        else:
            users = db.session.query(Users).all()
    else:
        users = db.session.query(Users).all()
    result = []
    for user1 in users:
        result.append({
            'admin_role_type' :user1.admin_role_type,
            'first_name':user1.first_name,
            'last_name': user1.last_name,
            'mobile_number': user1.mobile_number,
            'email_id': user1.email_id,
            'password': user1.password,
            'business_name': user1.business_name,
            'cr_number': user1.cr_number,
            'status': user1.status,
            'tax_certificate': user1.tax_certificate,
        })
    return jsonify(result)

@owner_bp.route('/<id>', methods=['GET'])
def get_user(id):
    user1 = db.session.query(Users).get(id)
    if user1:
        return jsonify({
            'admin_role_type' :user1.admin_role_type,
            'first_name':user1.first_name,
            'last_name': user1.last_name,
            'mobile_number': user1.mobile_number,
            'email_id': user1.email_id,
            'password': user1.password,
            'business_name': user1.business_name,
            'cr_number': user1.cr_number,
            'status': user1.status,
            'tax_certificate': user1.tax_certificate
        })
    return jsonify({'message': 'User not found'}), 404

@owner_bp.route('/addowner', methods=['POST'])
def create_user():
    data = request.get_json()

    email_exists = db.session.query(db.exists().where(Users.email_id == data.get('email_id', ''))).scalar()
    phone_exists = db.session.query(db.exists().where(Users.mobile_number == data.get('mobile_number', ''))).scalar()
    #emailexists
    if email_exists:
        return jsonify({'exists': True, 'email_exists': email_exists, 'message': 'Email already registered'}), 400
    #mobilenumberexists
    elif phone_exists:
        return jsonify({'exists': True, 'phone_exists': phone_exists, 'message': 'Phone number already registered'}), 400
    else:
    # Create a new user
        new_user = Users(admin_role_type=data['admin_role_type'],first_name=data['first_name'],last_name=data['last_name'],mobile_number=data['mobile_number'],email_id=data['email_id'],password=data['password'],business_name=data['business_name'],cr_number=data['cr_number'],status=data['status'],tax_certificate=data['tax_certificate'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201

@owner_bp.route('/updateowner/<id>', methods=['PUT'])
def update_user(id):
    user = db.session.query(Users).get(id)
    if user:
        data = request.get_json()
        user.admin_role_type = data['admin_role_type']
        user.first_name = data['first_name'],
        user.last_name = data['last_name'],
        user.mobile_number = data['mobile_number'],
        user.email_id = data['email_id'],
        user.password = data['password'],
        user.business_name = data['business_name'],
        user.cr_number = data['cr_number'],
        user.status = data['status'],
        user.tax_certificate = data['tax_certificate']
        db.session.commit()
        return jsonify({'message': 'User updated successfully'}), 200
    return jsonify({'message': 'User not found'}), 404


@owner_bp.route('/deleteowner/<id>', methods=['DELETE'])
def delete_user(id):
    user = db.session.query(Users).get(id)
    if user:
        if user.status == 1:
            user.status = 3
            db.session.commit()
            return jsonify({'message': 'User deleted successfully'}), 200
        else:
            return jsonify({'message': 'User is already deleted'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404
