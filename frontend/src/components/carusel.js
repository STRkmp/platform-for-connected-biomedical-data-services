import { Carousel } from 'antd';
import './mainPage.css';

const images = [
    {
        src: 'https://static10.tgstat.ru/channels/_0/c3/c373c2a626425ef70cec87e27af9fb4b.jpg',
        alt: 'Image 0',
    },
    {
        src: 'https://i.pinimg.com/originals/2d/38/28/2d3828491598131c664c96e7a36fd4f5.jpg',
        alt: 'Image 1'
    },
    {
        src: 'https://sun9-27.userapi.com/impg/itS64U-GtjgXRnqJSXwvkAtc_5jxnmBhg67RUQ/MINuZ8uQu5k.jpg?size=604x360&quality=96&sign=0e7ea2fcbfb74b68cedbf8b62e7fd80e&type=album',
        alt: 'Image 2'
    },
    {
        src: 'https://sun9-75.userapi.com/impg/GNR7XxdK_56DAQkx30eV1d-i3tMQhawdqSTedw/HEl1NDDo3Ek.jpg?size=1000x661&quality=96&sign=e6d99927ff0f64be817f79078a480549&c_uniq_tag=i7mRiKjj3dwk7l_j6WLmxakQWEnjzXIu-NkZBtR3WTE&type=album',
        alt: 'Image 3'
    }
];

const ImageCarousel = () => {
    return (
        <Carousel autoplay style={{ height: '100%', width: '100%' }}>
            {images.map((image, index) => (
                <div className="carousel-image" key={index}>
                    <img style={{ objectFit: 'contain', width: '100%', height: '80vh' }} src={image.src} alt={image.alt} />
                </div>
            ))}
        </Carousel>
    );
};

export default ImageCarousel;
