from flask import Blueprint, jsonify,request,render_template
from models.owner import Users,db
from models.category import Category
from models.store import Store_category,Store_timings
import json
from instance.response import SuccessJson,ErrorJson
from models import session
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_jwt_extended import create_access_token
from flask_cors import CORS
owner_bp = Blueprint('owner', __name__)

@owner_bp.route('/')
# @jwt_required()
def get_users():
    # currentID = get_jwt_identity()
    status_param = request.args.get('status')
    if status_param is not None:
        status = int(status_param)
        if status == 1:
            arr = session.query(Users).filter_by(status=1).all()
        else:
            arr = session.query(Users).all()
    else:
        arr = session.query(Users).all()
    result = []
    for ownerData in arr:
        result.append({
            'admin_role_type' :ownerData.admin_role_type,
            'first_name':ownerData.first_name,
            'last_name': ownerData.last_name,
            'mobile_number': ownerData.mobile_number,
            'email_id': ownerData.email_id,
            'password': ownerData.password,
            'business_name': ownerData.business_name,
            'cr_number': ownerData.cr_number,
            'status': ownerData.status,
            'tax_certificate': ownerData.tax_certificate,
        })
    session.close()
    return jsonify(result)

@owner_bp.route('/<id>', methods=['GET'])
@jwt_required()
def get_user(id):
    currentID = get_jwt_identity()
    arr = session.query(Users).get(id)
    if arr:
        session.close()
        return jsonify({
            'admin_role_type' :arr.admin_role_type,
            'first_name':arr.first_name,
            'last_name': arr.last_name,
            'mobile_number': arr.mobile_number,
            'email_id': arr.email_id,
            'password': arr.password,
            'business_name': arr.business_name,
            'cr_number': arr.cr_number,
            'status': arr.status,
            'tax_certificate': arr.tax_certificate
        })
    
    return jsonify({'message': 'User not found'}), 404

@owner_bp.route('/addowner', methods=['POST'])
@jwt_required()
def create_user():
    currentID = get_jwt_identity()
    data = request.get_json()

    email_exists = session.query(db.exists().where(Users.email_id == data.get('email_id', ''))).scalar()
    phone_exists = session.query(db.exists().where(Users.mobile_number == data.get('mobile_number', ''))).scalar()
    #emailexists
    if email_exists:
        return jsonify({'exists': True, 'email_exists': email_exists, 'message': 'Email already registered'}), 400
    #mobilenumberexists
    elif phone_exists:
        return jsonify({'exists': True, 'phone_exists': phone_exists, 'message': 'Phone number already registered'}), 400
    else:
    # Create a new user
        new_user = Users(admin_role_type=data['admin_role_type'],first_name=data['first_name'],last_name=data['last_name'],mobile_number=data['mobile_number'],email_id=data['email_id'],password=data['password'],business_name=data['business_name'],cr_number=data['cr_number'],status=data['status'],tax_certificate=data['tax_certificate'])
        session.add(new_user)
        session.commit()
        session.close()
        return jsonify({'message': 'User created successfully'}), 201

@owner_bp.route('/updateowner/<id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    currentID = get_jwt_identity()
    arr = session.query(Users).get(id)
    if arr:
        data = request.get_json()
        arr.admin_role_type = data['admin_role_type']
        arr.first_name = data['first_name'],
        arr.last_name = data['last_name'],
        arr.mobile_number = data['mobile_number'],
        arr.email_id = data['email_id'],
        arr.password = data['password'],
        arr.business_name = data['business_name'],
        arr.cr_number = data['cr_number'],
        arr.status = data['status'],
        arr.tax_certificate = data['tax_certificate']
        session.commit()
        session.close()
        return jsonify({'message': 'User updated successfully'}), 200
    return jsonify({'message': 'User not found'}), 404


@owner_bp.route('/deleteowner/<id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    currentID = get_jwt_identity()
    arr = session.query(Users).get(id)
    if arr:
        if arr.status == 1:
            arr.status = 3
            session.commit()
            session.close()
            return jsonify({'message': 'User deleted successfully'}), 200
        else:
            return jsonify({'message': 'User is already deleted'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404
    
    
@owner_bp.route('/getbyid/<id>')
@jwt_required()
def get_category(id):
    currentID = get_jwt_identity()
    arr = session.query(Users).filter_by(id=id).first()
    result = []
    
    ownerData = {
    "id": arr.id,
    'first_name':arr.first_name,
    "store": []
    }
    
    
    arr = session.query(Users).filter_by(parent_id=arr.id).all()
    # user_ids = [user.id for user in query_result]  # Get a list of all user IDs

    for store in arr:
        storeData = {
            "id": store.id,
            "first_name":store.first_name,
            "category": [],
            "time": []
        }
        ownerData["store"].append(storeData)
        arrCategory = session.query(Store_category).filter(Store_category.store_id == store.id).all()

        for category in arrCategory:
            categoryData = {
                "id": category.id,
                "store_id": category.store_id,
                "category_title": category.fk_store_category.title
            }

            storeData["category"].append(categoryData)
        
        arrStoreTime = session.query(Store_timings).filter(Store_timings.store_id == store.id).all()
        for storeTime in arrStoreTime:
            storeTimeData = {
                "id": storeTime.id,
                "store_id": storeTime.store_id,
                "category_title": storeTime.fk_store_timings.first_name
            }

            storeData["time"].append(storeTimeData)

        session.close()
    result.append(ownerData)
    
    return SuccessJson(result)

    
@owner_bp.route('/get')
@jwt_required()
def get_simple(): 
    currentID = get_jwt_identity()
    users = session.query(Users).all()  

    result = []
    for user in users:
        result.append({
            'first_name': user.first_name,
            'last_name': user.last_name,
            # Other attributes
        })

    session.close()  # Close the session after using it

    return jsonify(result)


@owner_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    first_name = data.get('first_name')
    password = data.get('password')

    if not first_name or not password:
        return jsonify(message='Invalid credentials'), 400

    user = Users.query.filter_by(first_name=first_name).first()

    if user and user.password == password:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token, message='Login successful')
    else:
        return jsonify(message='Invalid credentials'), 401
    