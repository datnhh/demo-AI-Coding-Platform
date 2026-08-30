namespace Demo;

/// <summary>
/// Vài phép biến đổi chuỗi đơn giản.
/// </summary>
/// <remarks>
/// Cố ý để trống chỗ cho việc mở rộng: repo này tồn tại để agent có thứ gì đó thật để sửa.
/// </remarks>
public static class StringUtils
{
    /// <summary>Đảo ngược một chuỗi.</summary>
    public static string Reverse(string value)
    {
        ArgumentNullException.ThrowIfNull(value);

        char[] characters = value.ToCharArray();
        Array.Reverse(characters);

        return new string(characters);
    }
}
