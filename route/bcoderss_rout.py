from flask import Blueprint, request
from pre_request import pre, Rule
import core.bcoderss as bcoderss
from util.json_util import return_json

bcoderss_route = Blueprint('bcoderss_route', __name__)

fields = {
    "tags": Rule(type=list, required=False, dest="tags"),
    "page": Rule(type=int, required=False, dest="page"),
    "size": Rule(type=int, required=False, dest="size"),
}


@bcoderss_route.route("/bcoderss/get_random_img_url", methods=["GET"])
@pre.catch(fields)
def get_random_img_url():
    tags = request.args.getlist('tags') if request.args.getlist('tags') else ['最新']
    page = request.args.get('page') if request.args.get('page') else 1
    return bcoderss.get_random_img_url(tags, page)


@bcoderss_route.route("/bcoderss/get_random_img_urls", methods=["GET"])
@pre.catch(fields)
@return_json
def get_random_img_urls():
    tags = request.args.getlist('tags') if request.args.getlist('tags') else ['最新']
    page = request.args.get('page') if request.args.get('page') else 1
    size = request.args.get('size') if request.args.get('size') else 1
    return bcoderss.get_random_img_urls(tags, page, size)
