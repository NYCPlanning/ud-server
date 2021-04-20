const { Site } = require('./generated/site_pb.js');
const { TaxLot } = require('./generated/model_base_pb.js');
const { SiteServiceClient } = require('./generated/site_grpc_web_pb.js');

var client = new SiteServiceClient('http://0.0.0.0:8088');

// create a TaxLot object for the request
var request = new TaxLot();
request.setBbl('1001230002');

// make a remote procedure call to get a Site object
client.makeSite(request, {}, (err, response) => {
  console.log(response.getId())
});
