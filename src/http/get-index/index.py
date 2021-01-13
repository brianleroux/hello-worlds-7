def handler (event, context):
  return {'statusCode':200, 'headers':{'content-type':'text/html'}, 'body': 'hey <b>here</b>' }
