from app import app
import datetime
from models import User, Listing, Location, Property, RentalTerms,  Review, UserFavoriteProperty,Payment, db

# Function to seed the database with sample data
def seed_data():
    # Clear the existing data from all tables
    User.query.delete()
    Listing.query.delete()
    Location.query.delete()
    Property.query.delete()
    RentalTerms.query.delete()
    Review.query.delete()
    UserFavoriteProperty.query.delete()
    Payment.query.delete()


    user1 = User(username='braxton', email='braxton@example.com', hashed_password='123456', role='tenant')
    user2 = User(username='shaffie', email='shaffie@example.com', hashed_password='123456', role='owner')
    

    db.session.add_all([user1, user2])
    db.session.commit()

    # Seed data for locations
    location1 = Location(city='mombasa', neighborhood='Neighborhood A', specific_area='Area A', latitude='0.000', longitude='0.000')
    location2 = Location(city='', neighborhood='Neighborhood B', specific_area='Area B', latitude='0.000', longitude='0.000')

    db.session.add_all([location1, location2])
    db.session.commit()
    
    
    
    
     # Seed data for listings
    listing_data = [
        {
            'id': 1,
            'location_id': 1,
            'title': 'Spacious Downtown Office Suite',
            'description': 'A modern and spacious office suite located in the heart of downtown. It features large windows for ample natural light, a reception area, three private offices, a conference room, and a break area. Perfect for a growing business.',
            'rent': '$3,400/month',
            'place': '4404 Brian Plains, Port Marie, IN 70903',
            'size': '1000 sqft',
            'utilities': 'High-speed WiFi, parking space, security (CCTV)',
            'media': 'https://cdn.pixabay.com/photo/2013/09/14/19/53/city-182223_640.jpg'
        },
        {
            'id': 2,
            'location_id': 2,
            'title': 'Cozy Studio Apartment near the Park',
            'description': 'This charming studio apartment is just a short walk from the local park. It offers an open floor plan with a fully equipped kitchen, a comfortable living area, and a separate sleeping area. Ideal for a single professional or student.',
            'rent': '$3,000/month',
            'place': '456 Elm Avenue, Parkside',
            'size': '500 sqft',
            'utilities': 'High-speed WiFi, parking space, security (CCTV)',
            'media': 'https://cdn.pixabay.com/photo/2019/03/08/20/14/kitchen-living-room-4043091_640.jpg'
        },
         {
        'id': 3,
        'title': 'Prime Retail Space on Main Street',
        'location_id': 3,
        'description': 'An excellent opportunity to lease a prime retail space on Main Street. The property features a spacious layout, large display windows, and high foot traffic. Ideal for a boutique, cafe, or specialty shop.',
        'rent': '$5,200/month',
        'place': '789 Main Street, Downtown',
        'size': '1500 sqft',
        'media': 'https://cdn.pixabay.com/photo/2015/08/25/11/50/shopping-mall-906721_640.jpg',
        'utilities': 'WiFi, parking space'
        },
        {
        'id': 4,
        'title': 'Luxury Penthouse with Stunning Views',
        'location_id': 4,
        'description': 'Experience luxury living in this exquisite penthouse apartment boasting breathtaking views of the city skyline. It offers high-end finishes, a gourmet kitchen, a private terrace, and access to exclusive amenities such as a fitness center and pool.',
        'rent': '$8,500/month',
        'place': '10 Highrise Avenue, Skyview Heights',
        'size': '2,800 square feet',
        'media': 'https://cdn.pixabay.com/photo/2014/06/21/20/16/real-estate-374107_1280.jpg',
        'utilities': 'WiFi, parking space, security (CCTV), back-up power'
         },
    {
        'id': 5,
        'title': 'Industrial Warehouse with Loading Dock',
        'location_id': 1,
        'description': 'This spacious industrial warehouse is equipped with a loading dock, high ceilings, and ample storage space. It\'s perfect for businesses requiring logistics support or additional inventory space.',
        'rent': '$4,000/month',
        'place': '111 Warehouse Lane, Industrial District',
        'size': '5,000 sqft',
        'media': 'https://cdn.pixabay.com/photo/2018/12/09/17/57/hall-3865370_1280.jpg',
        'utilities': 'Parking space, security (guardmen), back-up power'
    },
    {
        'id': 6,
        'title': 'Stylish 2-Bedroom Apartment in Trendy Neighborhood',
        'location_id': 5,
        'description': 'Embrace the vibrant city life in this stylish 2-bedroom apartment situated in a trendy neighborhood. It features a modern kitchen, spacious living area, and access to nearby restaurants, shops, and entertainment options.',
        'rent': '$1,000/month',
        'place': '222 Oak Street, Trendyville',
        'size': '900 square feet',
        'media': 'https://cdn.pixabay.com/photo/2014/07/31/21/41/apartment-406901_640.jpg',
        'utilities': 'WiFi, parking space'
    },
    {
        'id': 7,
        'title': 'Commercial Office Space with Flexible Layout',
        'location_id': 3,
        'description': 'This versatile commercial office space offers a flexible layout that can be customized to suit your business needs. It includes private offices, open work areas, a conference room, and a reception area. Conveniently located near major highways.',
        'rent': '$4,500/month',
        'place': '333 Business Boulevard, Business District',
        'size': '3500 sqft',
        'media': 'https://cdn.pixabay.com/photo/2015/11/15/20/49/modern-office-1044807_1280.jpg',
        'utilities': 'WiFi, parking space'
    },
    {
        'id': 8,
        'title': 'Quaint Cottage with Private Garden',
        'location_id': 2,
        'description': 'Escape to this charming cottage nestled in a serene neighborhood. It boasts a private garden, a cozy living area, a fully equipped kitchen, and two comfortable bedrooms. A perfect retreat for nature lovers.',
        'rent': '$1,800/month',
        'place': '252 Mark Plains, Dennisberg, IN 51233',
        'size': '1200 sqft',
        'media': 'https://cdn.pixabay.com/photo/2016/08/15/00/45/log-cabin-1594361_1280.jpg',
        'utilities': 'WiFi, parking space, security (CCTV), back-up power'
    },
    {
        'id': 9,
        'title': 'Retail Space in Busy Shopping Plaza',
        'location_id': 2,
        'description': 'Take advantage of this prime retail space located in a bustling shopping plaza. With high visibility and a steady flow of customers, it presents an excellent opportunity for your business to thrive.',
        'rent': '$3,800/month',
        'place': '555 Plaza Avenue, Shopper\'s Paradise',
        'size': '1000 sqft',
        'media': 'https://cdn.pixabay.com/photo/2018/10/15/14/58/cape-town-3749167_1280.jpg',
        'utilities': 'WiFi, parking space'
    },
    {
        'id': 10,
        'title': 'Modern Office Suite with River View',
        'location_id': 1,
        'description': 'Enjoy panoramic river views from this modern office suite. It offers a professional environment with a reception area, private offices, a conference room, and a break area. Conveniently located near downtown amenities.',
        'rent': '$3,800/month',
        'place': '666 Riverside Drive, Riverview Center',
        'size': '1500 sqft',
        'media': 'https://cdn.pixabay.com/photo/2016/10/16/10/30/office-space-1744803_640.jpg',
        'utilities': 'WiFi, parking space, security (CCTV), back-up power'
    }
      
    ]

    for listing in listing_data:
        new_listing = Listing(
            id=listing['id'],
            location_id=listing['location_id'],
            title=listing['title'],
            description=listing['description'],
            rent=listing['rent'],
            place=listing['place'],
            size=listing['size'],
            utilities=listing['utilities'],
            media=listing['media']
        )
        db.session.add(new_listing)

    db.session.commit()
    # Seed data for properties
    property1 = Property(
        property_type='Villa',
        property_category='Residential',
        property_title= 'A luxurious villa featuring 4 bedrooms, & 4 bathrooms',
        property_rent = 45600,
        bedrooms=4,
        bathrooms=4,
        amenities='Parking, Laundry Facilities, Air Conditioning, Security Systems, Swimming Pools',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2017/04/10/22/28/residence-2219972_640.jpg',
        images='https://cdn.pixabay.com/photo/2013/10/12/18/05/villa-194671_640.jpg, https://cdn.pixabay.com/photo/2020/04/17/12/28/pool-5055009_640.jpg, https://cdn.pixabay.com/photo/2015/11/06/11/45/interior-1026446_640.jpg, https://cdn.pixabay.com/photo/2016/10/13/09/06/travel-1737168_640.jpg, https://cdn.pixabay.com/photo/2015/11/06/11/45/interior-1026454_640.jpg, https://cdn.pixabay.com/photo/2016/10/13/09/08/travel-1737171_640.jpg, https://cdn.pixabay.com/photo/2020/03/21/20/04/real-estate-4955093_640.jpg, https://cdn.pixabay.com/photo/2017/03/30/00/24/villa-2186906_640.jpg',
        house_tour_video='https://static.videezy.com/system/resources/previews/000/052/461/original/alb_kaleido1007_1080p_24fps.mp4',
        property_documents=None,
        furnished='Yes',
        description='This is a luxurious villa available for rent in Kilimani, Nairobi, Kenya, at Kshs 45,600 per month. It features 4 bedrooms, 4 bathrooms, and amenities like parking, laundry facilities, air conditioning, security systems, and swimming pools. Close to schools and parks, it offers convenience for families. The owner, Jane Ngugi, can be contacted at +61 2 9876 5432 (WhatsApp too) or janengugi@gmail.com. The fully furnished villa includes a captivating house tour video. However, please note that pets are not allowed. With a beautiful garden and modern interior, this villa offers a luxurious and inviting home for residents.',
        location_details='Close to schools and parks.',
        location_id = 2,
        country='Kenya',
        city_town='Nairobi',
        neighborhood_area='Kilimani',
        address='456 Maple Ave, Kilimani, Nairobi',
        user_id = 2,
        property_owner_name='Jane Ngugi',
        property_owner_photo='https://cdn.pixabay.com/photo/2020/08/21/08/46/african-5505598_640.jpg',
        contact_phone='+61 2 9876 5432',
        contact_whatsapp='+61 2 9876 5432',
        contact_email='janengugi@gmail.com',
        facebook='facebook.com/maria.silva',
        twitter=None,
        instagram=None,
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='whatsapp',
        additional_details='The property management does not allow pets',
    )
    property2 = Property(
        property_type='Apartment',
        property_category='Residential',
        property_title= 'A modern apartment available for rent in Nairobi, Kenya. This residential gem offers two bedrooms, & one bathroom',
        property_rent = 30000,
        bedrooms=2,
        bathrooms=1,
        amenities='Parking, Elevator, Balcony, Gym',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2016/11/18/17/20/living-room-1835923_640.jpg',
        images= 'https://cdn.pixabay.com/photo/2017/12/27/14/41/window-3042834_640.jpg, https://cdn.pixabay.com/photo/2018/01/29/07/55/modern-minimalist-bathroom-3115450_640.jpg, https://cdn.pixabay.com/photo/2017/02/24/12/19/apartment-2094666_640.jpg, https://cdn.pixabay.com/photo/2014/08/11/21/31/wall-panel-416041_640.jpg, https://cdn.pixabay.com/photo/2015/11/07/21/29/livingroom-1032733_640.jpg, https://cdn.pixabay.com/photo/2017/12/27/14/42/furniture-3042835_640.jpg',
        house_tour_video='https://static.videezy.com/system/resources/previews/000/002/004/original/20140614-SoudertonPA-YellowFlowersBreeze.mp4',
        property_documents=None,
        furnished='No',
        description='This is a modern apartment available for rent in Nairobi, Kenya, at Kshs 30,000 per month. This residential gem offers two bedrooms, one bathroom, and comes with convenient amenities such as parking, an elevator, balcony, and gym. The main image displays a stylish living room, capturing the apartment contemporary ambiance. Located in the bustling Midtown area, the apartment is within walking distance to shopping and public transport, ensuring easy accessibility. The owner, Alex Johnson, can be contacted at +1 123-456-7890 or WhatsApp at +1 417-123-4567. For inquiries, reach out via email at alex@example.com. Social media enthusiasts can connect with Alex on Facebook, Twitter, and Instagram. The property features a captivating house tour video showcasing the apartments stunning view and desirable location. Pets are allowed with a deposit, making it a pet-friendly choice for tenants. With its modern design and convenient location, this apartment promises an exceptional living experience for those seeking contemporary city living.',
        location_details='Walking distance to shopping and public transport.',
        location_id = 1,
        country='Kenya',
        city_town='Nairobi',
        neighborhood_area='Midtown',
        address='789 Park Ave, Midtown, Nairobi',
        user_id = 1,
        property_owner_name='Alex Johnson',
        property_owner_photo='https://cdn.pixabay.com/photo/2022/01/23/23/43/couple-6962202_640.jpg',
        contact_phone='+1 123-456-7890',
        contact_whatsapp='+1 417-123-4567',
        contact_email='alex@example.com',
        facebook='facebook.com/alex.johnson',
        twitter='twitter.com/alex_johnson',
        instagram='instagram.com/alex.johnson',
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='email',
        additional_details='Pets allowed with deposit.',
    )
    property3 = Property(
        property_type='House',
        property_category='Residential',
        property_title= 'A spacious family home for rent, features four bedrooms, three and a half bathrooms',
        property_rent = 150600,
        bedrooms=4,
        bathrooms=3.5,
        amenities='Garage, Garden, Fireplace',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2014/07/31/00/30/vw-beetle-405876_640.jpg',
        images='https://cdn.pixabay.com/photo/2017/07/09/03/19/home-2486092_640.jpg, https://cdn.pixabay.com/photo/2016/08/26/15/06/home-1622401_640.jpg, https://cdn.pixabay.com/photo/2014/07/10/17/17/bedroom-389254_640.jpg, https://cdn.pixabay.com/photo/2016/01/31/14/32/architecture-1171462_640.jpg, https://cdn.pixabay.com/photo/2017/03/28/12/10/chairs-2181947_640.jpg, https://cdn.pixabay.com/photo/2017/08/02/01/01/living-room-2569325_640.jpg, https://cdn.pixabay.com/photo/2015/10/20/18/57/furniture-998265_640.jpg',
        house_tour_video= 'https://static.videezy.com/system/resources/previews/000/053/090/original/alb_kaleido1068_1080p.mp4',
        property_documents='https://example.com/documents/property2.pdf',
        furnished='Yes',
        description='This is a spacious family home for rent in Nairobi, Kenya, at Kshs 150,600 per month. It features four bedrooms, three and a half bathrooms, and modern amenities like a garage, garden, and fireplace. The main image showcases a vintage VW Beetle, adding to its unique charm. The interior has a warm and inviting atmosphere with modern design. Located in a quiet Suburbia neighborhood, the house is close to schools and parks, ideal for families. The owner, David Smith, can be reached at +1 416-555-1234 or WhatsApp at +1 418-555-1234. Contact email is david@example.com, and WhatsApp is the preferred method. The property offers a virtual house tour video and documents available at example.com/documents/property2.pdf. Open house events are held on weekends. This family home presents an exceptional living experience with its spacious layout, beautiful garden, and modern amenities in a serene and convenient Nairobi location.',
        location_details='Quiet neighborhood near schools and parks.',
        location_id = 2,
        country='Kenya',
        city_town='Nairobi',
        neighborhood_area='Suburbia',
        address='123 Maple St, Suburbia, Nairobi ',
        user_id = 2,
        property_owner_name='David Smith',
        property_owner_photo='https://cdn.pixabay.com/photo/2017/02/16/23/10/smile-2072907_640.jpg',
        contact_phone='+1 416-555-1234',
        contact_whatsapp='+1 418-555-1234',
        contact_email='david@example.com',
        facebook=None,
        twitter=None,
        instagram=None,
        linkedin='linkedin.com/in/david-smith',
        other_social_media=None,
        preferred_contact_method='whatsapp',
        additional_details='Open house on weekends.',
    )
    property4 = Property(
        property_type='Condo',
        property_title= 'A cozy and modern one-bedroom condo located in Nairobi',
        property_category='Residential',
        property_rent = 16700,
        bedrooms=1,
        bathrooms=1,
        amenities='Swimming Pool, Fitness Center',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2019/12/17/04/52/lounge-4700728_640.jpg',
        images='https://cdn.pixabay.com/photo/2019/03/08/20/14/kitchen-living-room-4043091_640.jpg, https://cdn.pixabay.com/photo/2023/01/10/20/56/nyc-7710506_1280.jpg, https://cdn.pixabay.com/photo/2016/11/18/17/20/living-room-1835923_640.jpg, https://cdn.pixabay.com/photo/2014/08/11/21/39/wall-416060_640.jpg',
        house_tour_video=None,
        property_documents=None,
        furnished='Yes',
        description='This is a cozy and modern condo located in Nairobi, Kenya, available for rent at Kshs 16,700 per month. This residential property offers one bedroom and one bathroom, making it an ideal choice for individuals or couples. The condo comes furnished and includes amenities such as a swimming pool and fitness center, providing residents with opportunities for relaxation and fitness. The main image showcases the inviting lounge area, setting the tone for a comfortable living space. The condo is situated in a serene environment close to downtown Nairobi, with convenient access to public transportation. Downtown amenities are easily accessible, making daily activities and entertainment readily available to residents. The owner, Maria Salim, can be contacted via phone at +1 418-123-4567 or through WhatsApp at +1 415-123-4567. Her preferred contact method is phone. For further details or to arrange a viewing, interested parties can reach out to Maria at maria@example.com. The rent includes utilities, making it convenient for tenants. With its prime location, modern amenities, and serene environment, this cozy condo offers an excellent living experience for those seeking a comfortable and well-equipped home in Nairobi.',
        location_details='Close to downtown and public transportation.',
        location_id = 1,
        country='Kenya',
        city_town='Nairobi',
        neighborhood_area='Downtown',
        address='456 Elm St, Downtown, Nairobi',
        property_owner_name='Maria Salim',
        user_id = 1,
        property_owner_photo='https://cdn.pixabay.com/photo/2019/11/04/19/51/hands-4602022_640.jpg',
        contact_phone='+1 418-123-4567',
        contact_whatsapp='+1 415-123-4567',
        contact_email='maria@example.com',
        facebook='facebook.com/maria.salim',
        twitter=None,
        instagram=None,
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='phone',
        additional_details='Utilities included in rent.',
    )
    property5 = Property(
        property_type='Studio',
        property_title= 'A charming studio apartment in Nakuru, Kenya, with 1 bedroom and a single bathroom',
        property_category='Residential',
        property_rent = 20000,
        bedrooms=0,
        bathrooms=1,
        amenities='Laundry Facilities, High-speed Internet',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2013/09/24/11/06/house-185714_640.jpg',
        images= 'https://cdn.pixabay.com/photo/2018/06/26/15/56/condo-3499679_640.jpg, https://cdn.pixabay.com/photo/2019/12/26/16/51/luxury-suite-4720815_640.jpg, https://cdn.pixabay.com/photo/2017/03/19/01/18/living-room-2155353_640.jpg, https://cdn.pixabay.com/photo/2017/03/19/01/43/living-room-2155376_1280.jpg',
        house_tour_video= 'https://static.videezy.com/system/resources/previews/000/004/382/original/COWS_AT_THE_GRASS.mp4',
        property_documents=None,
        furnished='Yes',
        description='This is a charming studio apartment in Nakuru, Kenya, available for rent at Kshs 20,000 per month. It offers a single bathroom, laundry facilities, and high-speed internet. The studio is furnished and equipped with all the essentials for comfortable living. The main image showcases the exterior of the building. Conveniently located in the city center, the studio provides easy access to public transport, cafes, and shops. The area is bustling with amenities, making it an ideal choice for those seeking a lively urban lifestyle. The owner, Sophie Turner, can be contacted via phone or WhatsApp at +254 708276919 or through email at sophie@example.com. She is also available on Instagram at instagram.com/sophie_turner. The preferred contact method is email. Please note that pets are not allowed in the studio. With its prime location and essential amenities, this studio apartment is perfect for individuals looking for a cozy and well-connected living space in the heart of Nakuru.',
        location_details='In the heart of the city, near cafes and shops.',
        location_id = 2,
        country='Kenya',
        city_town='Nakuru',
        neighborhood_area='City Center',
        address='789 Oxford St, Highlands, Nakuru',
        user_id = 2,
        property_owner_name='Sophie Turner',
        property_owner_photo= 'https://cdn.pixabay.com/photo/2017/02/16/23/10/smile-2072907_640.jpg',
        contact_phone= '+254 708276919',
        contact_whatsapp= '+254 708276919',
        contact_email='sophie@example.com',
        facebook=None,
        twitter='twitter.com/sophie_turner',
        instagram='instagram.com/sophie_turner',
        linkedin=None,
        other_social_media=None,
        preferred_contact_method='email',
        additional_details='No pets allowed.',
    )
    property6 = Property(
        property_title= 'This is a 3-bedroomed townhouse located in Mombasa, Kenya, available for rent at Kshs 20,000 per month',
        property_type='Townhouse',
        property_category='Residential',
        property_rent = 20000,
        bedrooms=3,
        bathrooms=2.5,
        amenities='Garage, Patio',
        square_footage=None,
        main_image='https://cdn.pixabay.com/photo/2016/07/05/13/02/elegant-1498631_640.jpg',
        images='https://cdn.pixabay.com/photo/2017/01/14/12/48/hotel-1979406_640.jpg, https://pixabay.com/photos/living-room-sofa-couch-2569325/,https://pixabay.com/photos/living-room-interior-design-1835923/, https://cdn.pixabay.com/photo/2016/12/30/07/55/bedroom-1940169_640.jpg, https://cdn.pixabay.com/photo/2016/12/30/07/55/bedroom-1940169_640.jpg, https://cdn.pixabay.com/photo/2014/10/16/08/41/bathroom-490781_640.jpg, https://cdn.pixabay.com/photo/2018/08/21/23/35/bath-3622540_640.jpg, https://cdn.pixabay.com/photo/2016/12/30/07/59/kitchen-1940174_640.jpg',
        house_tour_video= 'https://static.videezy.com/system/resources/previews/000/038/659/original/alb_glitch1045_1080p_24fps.mp4',
        property_documents=None,
        furnished='No',
        description='This is a residential townhouse located in Mombasa, Kenya, available for rent at Kshs 20,000 per month. It offers three bedrooms, two and a half bathrooms, a garage, and a patio. The property is unfurnished and has modern features, including an elegant interior and recent renovations. The main image showcases the townhouse exterior.The property is situated in a family-friendly suburb with easy access to parks and schools. The owner, Michael Brown, can be contacted via phone or WhatsApp at +61 2 8765 4321 or through email at michael@gmail.com. The preferred contact method is via phone.With its spacious layout and outdoor space, this townhouse provides a comfortable living environment for potential tenants. It is an excellent option for those seeking a quality home in a peaceful and convenient location.',
        location_id = 1,
        location_details='Family-friendly neighborhood with parks and schools.',
        country='Kenya',
        city_town='Mombasa',
        neighborhood_area='Suburb',
        address='567 Park St, Bamburi, Mombasa',
        user_id = 1,
        property_owner_name='Michael Brown',
        property_owner_photo = 'https://cdn.pixabay.com/photo/2020/08/21/08/46/african-5505598_640.jpg',
        contact_phone='+61 2 8765 4321',
        contact_whatsapp= '+61 2 8765 4321',
        contact_email='michael@gmail.com',
        facebook=None,
        twitter='twitter.com/michael_brown',
        instagram=None,
        linkedin='linkedin.com/in/michael-brown',
        other_social_media=None,
        preferred_contact_method='phone',
        additional_details='Recent renovations.',
    )

    db.session.add_all([property1, property2, property3, property4, property5, property6])
    db.session.commit()
    
    
    payment1 = Payment(
        user_id=user1.id,
        property_id=property2.id,
        amount=1200.0,
        payment_method='Credit Card',
    )
    payment2 = Payment(
        user_id=user2.id,
        property_id=property1.id,
        amount=800.0,
        payment_method='M-Pesa',
    )

    db.session.add_all([payment1, payment2])
    db.session.commit()
    # Seed data for rental terms
    rental_terms1 = RentalTerms(
        property_id=property1.id,
        rental_price=3500,
        security_deposit=1000,
        lease_duration_min=12,
        lease_duration_max=24,
        additional_fees='None'
    )
    rental_terms2 = RentalTerms(
        property_id=property2.id,
        rental_price=1200,
        security_deposit=800,
        lease_duration_min=6,
        lease_duration_max=12,
        additional_fees='Utilities not included'
    )

    db.session.add_all([rental_terms1, rental_terms2])
    db.session.commit()


    # Seed data for reviews
    review1 = Review(user_id=user1.id, property_id=property1.id, full_name='Gloriah Kadimane', address='303, Thika Road, Kamakis, Nairobi', email='Gloriahkadimane@gmail.com', comment='Great office space!')
    review2 = Review(user_id=user2.id, property_id=property2.id, full_name='Joyce Njoroge', address='46723, Eastleigh, Nairobi', email='Joycenjoroge@gmail.com', comment='Cozy apartment with a lovely view.')

    db.session.add_all([review1, review2])
    db.session.commit()

    # Seed data for user favorite properties
    user_favorite_property1 = UserFavoriteProperty(user_id=user1.id, listing_id=None, property_id=property2.id)
    user_favorite_property2 = UserFavoriteProperty(user_id=user2.id, listing_id=None, property_id=property1.id)

    db.session.add_all([user_favorite_property1, user_favorite_property2])
    db.session.commit()
    
    

# Run the seed function
if __name__ == '__main__':
    with app.app_context():
        seed_data()
