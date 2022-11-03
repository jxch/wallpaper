from flask import Blueprint, request
from pre_request import pre, Rule
import core.bcoderss as bcoderss

bcoderss_route = Blueprint('bcoderss_route', __name__)

fields = {
    "tag": Rule(type=str, required=True, dest="tag"),
    "page": Rule(type=int, required=True, dest="page"),
}


@bcoderss_route.route("/bcoderss/get_random_img_url", methods=["GET"])
@pre.catch(fields)
def get_random_img_url():
    tag = request.args.get('tag')
    page = request.args.get('page')
    return bcoderss.get_random_img_url(tag, page)
