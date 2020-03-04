import xml.etree.ElementTree as ET
import urllib.request 
#request_url = urllib.request.urlopen('https://entapp.g.comcast.net/EntitlementService/device?macAddress=cc:40:d0:2f:9a:e0') 
#data = (request_url.read()) 
data = '''
<EntitlementResponse>
<TrackingId>ENTAPP-WC-D6P-7011-xcal.es.2020-03-03.19:15:04.800</TrackingId>
<Identities>
<Identity>
<Id>475829310120022012Comcast.USRIMS</Id>
<UID>lhodecker1010</UID>
<FirstName>LINDA</FirstName>
<LastName>HODECKER</LastName>
<Role>P</Role>
<LoginStatus>A</LoginStatus>
</Identity>
<Identity>
<Id>2361094548016221627052018.cust</Id>
<UID>mchristofasexstreme</UID>
<FirstName>Mike</FirstName>
<LastName>Christofas</LastName>
<Role>SMS</Role>
<LoginStatus>A</LoginStatus>
</Identity>
</Identities>
<Accounts>
<Account>
<Id>912138101414112007RL</Id>
<Number>8499050200034847</Number>
<BillingSystemId>CSG</BillingSystemId>
<Status>A</Status>
<isPreActive>False</isPreActive>
<AccountCreateDate>2001-03-29</AccountCreateDate>
<AccountType>R</AccountType>
<AccountDelinquencyStatus>Normal</AccountDelinquencyStatus>
<DetailedAccountStatus>Active</DetailedAccountStatus>
<AccountHoldStatus>NO_HOLD</AccountHoldStatus>
<LastUpdateTimestamp>2019-10-13T20:24:12.0Z</LastUpdateTimestamp>
<LastUpdateSystem>RTVE</LastUpdateSystem>
<CustomerCategorizations>
<CustomerCategorization>XCAL</CustomerCategorization>
</CustomerCategorizations>
<LineOfBusinessStatus>
<LOBStatus>
<LineOfBusiness>V</LineOfBusiness>
<Status>A</Status>
</LOBStatus>
<LOBStatus>
<LineOfBusiness>H</LineOfBusiness>
<Status>A</Status>
</LOBStatus>
<LOBStatus>
<LineOfBusiness>C</LineOfBusiness>
<Status>A</Status>
</LOBStatus>
</LineOfBusinessStatus>
<rateCodes>
DF018 HF012 TS012 TS014 TS016 TS017 TS018 TS019 TS020 TS021 TS022 TS023 TS024 TS025 TS026 TS027 TS028 TS029 TS034 TS036 TS037 TS038 TS058 TS060 TS061 TS062 TS063 TS064 TS076 AT201 VF065 VF075 VT650 HS248 HS249 VB006 VD018 VF123 VS001 VS002 VT163 TS059 VD076 VF171 VF173
</rateCodes>
<ServiceLocationInfo>
<Id>204478832</Id>
<AddressLine1>1010 BAY DR</AddressLine1>
<City>PLEASANTVILLE</City>
<State>NJ</State>
<Zip>08232</Zip>
</ServiceLocationInfo>
<ContactInfo>
<DisplayName>LINDA HODECKER</DisplayName>
<FirstName>LINDA</FirstName>
<LastName>HODECKER</LastName>
<HomePhone>6103499996</HomePhone>
<BusinessPhone>6093839491</BusinessPhone>
<OtherPhones>
<PhoneNumber>
<Number>6093839491</Number>
<Type>Additional Number</Type>
</PhoneNumber>
<PhoneNumber>
<Number>6103499996</Number>
<Type>Additional Number</Type>
</PhoneNumber>
<PhoneNumber>
<Number>6093839491</Number>
<Type>CDV Number</Type>
</PhoneNumber>
</OtherPhones>
</ContactInfo>
<DeviceProducts source="ESD">
<DeviceProduct>
<ComponentGuid>122552541328102011DV</ComponentGuid>
<DeviceCreateDate>2011-10-28</DeviceCreateDate>
<DeviceStatus>A</DeviceStatus>
<LastUpdateTimestamp>2019-10-13T20:24:11.0Z</LastUpdateTimestamp>
<LastUpdateSystem>RTVE</LastUpdateSystem>
<DeviceStatusDescription>ACTIVE</DeviceStatusDescription>
<EquipmentType>MW</EquipmentType>
<ComponentType>ESTB</ComponentType>
<ComponentMake>PC</ComponentMake>
<ComponentModel>PCRN150NR</ComponentModel>
<ComponentMode>LEGACY</ComponentMode>
<SerialNumber>M11049TD1320</SerialNumber>
<CCSerialNumber>MA1044FFQ743</CCSerialNumber>
<SubComponents>
<SubComponent>
<Status>A</Status>
<StatusDescription>ACTIVE</StatusDescription>
<SerialNumber>MA1044FFQ743</SerialNumber>
<MacAddress>00:00:02:C7:25:4E</MacAddress>
<Type>CC</Type>
</SubComponent>
<SubComponent>
<Status>A</Status>
<StatusDescription>ACTIVE</StatusDescription>
<MacAddress>00:25:F1:D3:87:56</MacAddress>
<Type>CM</Type>
</SubComponent>
<SubComponent>
<Status>A</Status>
<StatusDescription>ACTIVE</StatusDescription>
<MacAddress>E4:83:99:DB:4A:B6</MacAddress>
<Type>ESTB</Type>
</SubComponent>
</SubComponents>
</DeviceProduct>
<DeviceProduct>
<ComponentGuid>9203069746500291923062018.IMSP</ComponentGuid>
<DeviceCreateDate>2018-06-23</DeviceCreateDate>
<DeviceStatus>A</DeviceStatus>
<LastUpdateTimestamp>2019-10-13T20:24:12.0Z</LastUpdateTimestamp>
<LastUpdateSystem>RTVE</LastUpdateSystem>
<DeviceStatusDescription>ACTIVE</DeviceStatusDescription>
<EquipmentType>D4</EquipmentType>
<ComponentType>CM</ComponentType>
<ComponentMake>NETGEAR</ComponentMake>
<ComponentModel>c3700100nas</ComponentModel>
<ComponentMode>CM</ComponentMode>
<ComponentMacAddress>CC:40:D0:2F:9A:E0</ComponentMacAddress>
<SerialNumber>CC40D02F9AE0</SerialNumber>
<CpeDHCPCriteria>NA</CpeDHCPCriteria>
</DeviceProduct>
<DeviceProduct>
<ComponentGuid>915229450412072019Comcast.RTVE</ComponentGuid>
<DeviceCreateDate>2019-07-12</DeviceCreateDate>
<DeviceStatus>A</DeviceStatus>
<LastUpdateTimestamp>2019-10-13T20:24:12.0Z</LastUpdateTimestamp>
<LastUpdateSystem>RTVE</LastUpdateSystem>
<DeviceStatusDescription>ACTIVE</DeviceStatusDescription>
<EquipmentType>M7</EquipmentType>
<ComponentType>STB</ComponentType>
<ComponentMake>PC</ComponentMake>
<ComponentModel>ARPCXDTA</ComponentModel>
<ComponentMode>LEGACY</ComponentMode>
<ComponentMacAddress>00:BF:60:33:98:59</ComponentMacAddress>
<SerialNumber>PAX500005317</SerialNumber>
<ComponentUnitAddress>00001911613994073228</ComponentUnitAddress>
</DeviceProduct>
<DeviceProduct>
<ComponentGuid>329845580412072019Comcast.RTVE</ComponentGuid>
<DeviceCreateDate>2019-07-12</DeviceCreateDate>
<LastUpdateTimestamp>2019-10-13T20:24:12.0Z</LastUpdateTimestamp>
<LastUpdateSystem>RTVE</LastUpdateSystem>
<EquipmentType>UA</EquipmentType>
<ComponentType>EMTA</ComponentType>
<ComponentMake>ARRIS Group, Inc.</ComponentMake>
<ComponentModel>tg1682g</ComponentModel>
<ComponentMode>eMTA</ComponentMode>
<SerialNumber>5C8FE0434BF2</SerialNumber>
<SubComponents>
<SubComponent>
<Status>A</Status>
<StatusDescription>ACTIVE</StatusDescription>
<MacAddress>5C:8F:E0:43:4B:F2</MacAddress>
<Type>CM</Type>
</SubComponent>
<SubComponent>
<Status>A</Status>
<StatusDescription>ACTIVE</StatusDescription>
<MacAddress>5C:8F:E0:43:4B:F3</MacAddress>
<Type>MTA</Type>
</SubComponent>
</SubComponents>
</DeviceProduct>
<DeviceProduct>
<ComponentGuid>677852580211082019Comcast.RTVE</ComponentGuid>
<DeviceCreateDate>2019-08-11</DeviceCreateDate>
<DeviceStatus>A</DeviceStatus>
<LastUpdateTimestamp>2019-10-13T20:24:11.0Z</LastUpdateTimestamp>
<LastUpdateSystem>RTVE</LastUpdateSystem>
<DeviceStatusDescription>ACTIVE</DeviceStatusDescription>
<EquipmentType>M3</EquipmentType>
<ComponentType>STB</ComponentType>
<ComponentMake>MO</ComponentMake>
<ComponentModel>MOHDUDTA</ComponentModel>
<ComponentMode>LEGACY</ComponentMode>
<ComponentMacAddress>00:BF:01:46:0B:4C</ComponentMacAddress>
<SerialNumber>M1542EW13274</SerialNumber>
<ComponentUnitAddress>00001910021367628155</ComponentUnitAddress>
</DeviceProduct>
</DeviceProducts>
<AccountProducts source="ESD">
<ProductInfo>
<Number>6255</Number>
<ShortDescription>Universal Caller ID</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>22033</Number>
<ShortDescription>CDV Revenue (Non Sub)</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>30500024</Number>
<ShortDescription>XV/XI Customer Owned Equipment</ShortDescription>
<Type>Equipment</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>2154</Number>
<ShortDescription>Remote</ShortDescription>
<Type>Equipment</Type>
<LineOfBusiness>VIDEO</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000090</Number>
<ShortDescription>Operator Assisted Domestic LD</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000052</Number>
<ShortDescription>3 Way Calling</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000053</Number>
<ShortDescription>Anonymous Call Rejection</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000110</Number>
<ShortDescription>VM Call Forward Busy</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000111</Number>
<ShortDescription>VM Call Forward No Answer</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000112</Number>
<ShortDescription>Call Forward Selective</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000113</Number>
<ShortDescription>Call Forward Variable</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000059</Number>
<ShortDescription>Repeat Dialing</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>22008</Number>
<ShortDescription>Caller ID on PC</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>30400047</Number>
<ShortDescription>Unlimited Select</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8100</Number>
<ShortDescription>Telephone Number</ShortDescription>
<Type>Resource</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>30500013</Number>
<ShortDescription>Wireless Gateway XB3-XV</ShortDescription>
<Type>Equipment</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>99911101</Number>
<ShortDescription>Tracking Code</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VIDEO</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>22002</Number>
<ShortDescription>Published Listing</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>22004</Number>
<ShortDescription>CSG- Provisioning CDV</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000083</Number>
<ShortDescription>International Calling</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000084</Number>
<ShortDescription>International DA</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000063</Number>
<ShortDescription>Speed Dial 30</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000064</Number>
<ShortDescription>Speed Dial 8</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000086</Number>
<ShortDescription>Residential Local Line - Primary</ShortDescription>
<Type>Service</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000043</Number>
<ShortDescription>VM MWI</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000065</Number>
<ShortDescription>Standard Directory Listing - 1</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000001</Number>
<ShortDescription>Call ID Block Per Call</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000002</Number>
<ShortDescription>Call Return</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000003</Number>
<ShortDescription>Call Screening</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000004</Number>
<ShortDescription>Call Trace</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000005</Number>
<ShortDescription>Call Waiting</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000006</Number>
<ShortDescription>Call Waiting on Caller ID</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000007</Number>
<ShortDescription>Caller ID</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>20035</Number>
<ShortDescription>HD Technology Fee</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VIDEO</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>200000189</Number>
<ShortDescription>Digital Starter (Feature)</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VIDEO</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>7012</Number>
<ShortDescription>Basic Video (B1)</ShortDescription>
<Type>Service</Type>
<LineOfBusiness>VIDEO</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>7014</Number>
<ShortDescription>Expanded Video (B2)</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VIDEO</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>20400080</Number>
<ShortDescription>Performance Pro Tier</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>HIGH_SPEED_DATA</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>10400039</Number>
<ShortDescription>X1 Platform</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VIDEO</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>20300183</Number>
<ShortDescription>HSD Performance Pro</ShortDescription>
<Type>Service</Type>
<LineOfBusiness>HIGH_SPEED_DATA</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>8000071</Number>
<ShortDescription>Dig STB</ShortDescription>
<Type>Equipment</Type>
<LineOfBusiness>VIDEO</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>2862</Number>
<ShortDescription>DTA Converter</ShortDescription>
<Type>Equipment</Type>
<LineOfBusiness>VIDEO</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>20068</Number>
<ShortDescription>DTA Service</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VIDEO</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>30400034</Number>
<ShortDescription>Voice 2go (Feature)</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>30400033</Number>
<ShortDescription>Single Number Service (SNS)</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
<ProductInfo>
<Number>30400001</Number>
<ShortDescription>Text Messaging</ShortDescription>
<Type>Feature</Type>
<LineOfBusiness>VO_IP</LineOfBusiness>
</ProductInfo>
</AccountProducts>
<LogicalProducts>
<LogicalProduct>
<ResourceGuid>486903430223022012Comcast.IMS</ResourceGuid>
</LogicalProduct>
</LogicalProducts>
</Account>
</Accounts>
<CompleteResponse>true</CompleteResponse>
</EntitlementResponse>'''
print()

# myroot = mytree.getroot()
tree = ET.fromstring(data)
lst = tree.findall('Identities/Identity')
lsr = tree.findall('Accounts/Account')
for item in lst:
    print('Name:',item.find('FirstName').text,item.find('LastName').text)
    
    for items in lsr:
        print('BillingSystemId:',items.find('BillingSystemId').text)
        print('BillingAccountNumber:',items.find('Number').text)
    print('Role:',item.find('Role').text)

    print()
# for items in lsr:
#     print('BillingSystemId:',items.find('BillingSystemId').text)
#print ('Attr:',tree.find('email').get('hide'))

